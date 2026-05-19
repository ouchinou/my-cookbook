"""
publish.py — Vérifie, met à jour les index, commit et pousse les recettes.

Usage :
  python publish.py           # vérifie, index, commit, push
  python publish.py --fix     # corrige les noms invalides avant de publier
  python publish.py --dry-run # affiche le message de commit sans rien pousser
"""

import os
import subprocess
import sys
import tempfile

# ---------------------------------------------------------------------------
# Dossiers de recettes reconnus
# ---------------------------------------------------------------------------
RECIPE_FOLDERS = {
    "aperos",
    "entrees",
    "plats",
    "boulangerie_pates",
    "sauces",
    "bbq",
    "desserts",
}

MAX_TITLES_IN_MSG = 5  # Au-delà, on résume par "et N autres"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def run(cmd, capture=False, check=True):
    """Exécute une commande shell et retourne le résultat."""
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"  # force UTF-8 dans les sous-processus Python
    result = subprocess.run(
        cmd, shell=True, capture_output=capture, text=True, encoding="utf-8", env=env
    )
    if check and result.returncode != 0:
        if capture:
            sys.stderr.write(result.stderr)
        sys.exit(result.returncode)
    return result


def is_recipe_file(path):
    """Vrai si le chemin est une recette .md (pas un README, pas un script)."""
    path = path.replace("\\", "/").lstrip("/")
    if not path.endswith(".md"):
        return False
    if os.path.basename(path).lower() == "readme.md":
        return False
    top = path.split("/")[0]
    return top in RECIPE_FOLDERS


def get_recipe_title(filepath):
    """Extrait le titre H1 du fichier ; fallback sur le nom de fichier."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()
                if stripped.startswith("# "):
                    return stripped[2:].strip()
    except Exception:
        pass
    return (
        os.path.basename(filepath)
        .replace(".md", "")
        .replace("-", " ")
        .replace("_", " ")
        .title()
    )


def format_titles(titles):
    """Formate une liste de titres en tenant compte de MAX_TITLES_IN_MSG."""
    if len(titles) <= MAX_TITLES_IN_MSG:
        return ", ".join(titles)
    shown = ", ".join(titles[:MAX_TITLES_IN_MSG])
    return f"{shown} et {len(titles) - MAX_TITLES_IN_MSG} autre(s)"


# ---------------------------------------------------------------------------
# Construction du message de commit
# ---------------------------------------------------------------------------


def build_commit_message():
    """Analyse git status --porcelain et génère un message de commit."""
    result = run("git status --porcelain", capture=True, check=False)

    added, modified, deleted = [], [], []

    for line in result.stdout.splitlines():
        if len(line) < 4:
            continue

        xy = line[:2]  # Ex: "??", " M", "A ", "R ", "D "
        filepath = line[3:].strip()

        # Les renames sont au format "old -> new"
        if " -> " in filepath:
            filepath = filepath.split(" -> ")[1].strip()

        if not is_recipe_file(filepath):
            continue

        title = (
            get_recipe_title(filepath)
            if os.path.exists(filepath)
            else (
                os.path.basename(filepath).replace(".md", "").replace("-", " ").title()
            )
        )

        if "?" in xy or "A" in xy:
            added.append(title)
        elif "D" in xy:
            deleted.append(title)
        elif "M" in xy or "R" in xy:
            modified.append(title)

    parts = []
    if added:
        n = len(added)
        parts.append(
            f"ajout {n} recette{'s' if n > 1 else ''} : {format_titles(added)}"
        )
    if modified:
        n = len(modified)
        parts.append(
            f"màj {n} recette{'s' if n > 1 else ''} : {format_titles(modified)}"
        )
    if deleted:
        n = len(deleted)
        parts.append(
            f"suppression {n} recette{'s' if n > 1 else ''} : {format_titles(deleted)}"
        )

    if not parts:
        return "chore: mise à jour des index et scripts"

    prefix = "feat" if added else "fix"
    return f"{prefix}: " + " | ".join(parts)


# ---------------------------------------------------------------------------
# Pipeline principal
# ---------------------------------------------------------------------------


def main():
    auto_fix = "--fix" in sys.argv
    dry_run = "--dry-run" in sys.argv

    print("=" * 58)
    print("  🚀  Publication du carnet de recettes")
    print("=" * 58)

    # ── Étape 1 : vérification (+ correction optionnelle) ──────────────────
    check_cmd = (
        "python check_recipes.py --fix" if auto_fix else "python check_recipes.py"
    )
    print(
        f"\n📋 Étape 1/4 — Vérification des recettes{' (--fix)' if auto_fix else ''}..."
    )
    result = run(check_cmd, capture=True, check=False)
    print(result.stdout.rstrip())
    if result.returncode != 0:
        sys.stderr.write(result.stderr)
        print("\n❌ Publication annulée : des recettes sont invalides.")
        print(
            "   Conseil : relancez avec --fix pour corriger les noms automatiquement."
        )
        sys.exit(1)

    # ── Étape 2 : vérifier s'il y a quelque chose à publier ────────────────
    status = run("git status --porcelain", capture=True, check=False)
    if not status.stdout.strip():
        print("\nℹ️  Rien à publier, le dépôt est déjà à jour.")
        sys.exit(0)

    # ── Étape 3 : message de commit (avant update_readme pour ne pas polluer) ──
    print("\n📝 Étape 2/4 — Analyse des changements...")
    commit_msg = build_commit_message()
    print(f"   Message : {commit_msg}")

    # ── Étape 4 : mise à jour des index ───────────────────────────────────
    print("\n📄 Étape 3/4 — Mise à jour des index README...")
    result = run("python update_readme.py", capture=True, check=False)
    print(result.stdout.rstrip())

    if dry_run:
        print("\n⚠️  Mode --dry-run : aucun commit effectué.")
        sys.exit(0)

    # ── Étape 5 : git add → commit → push ─────────────────────────────────
    print("\n🚀 Étape 4/4 — Commit & push...")
    run("git add -A")

    # Écriture du message dans un fichier temporaire pour éviter les
    # problèmes d'encodage / guillemets sur Windows avec shell=True.
    tmp = tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", suffix=".txt", delete=False
    )
    try:
        tmp.write(commit_msg)
        tmp.close()
        result = run(f'git commit -F "{tmp.name}"', capture=True, check=False)
    finally:
        os.unlink(tmp.name)
    output = result.stdout.strip()
    if output:
        print(f"   {output}")
    if result.returncode != 0:
        if "nothing to commit" in result.stdout:
            print("   ℹ️  Rien à committer.")
            sys.exit(0)
        sys.stderr.write(result.stderr)
        sys.exit(result.returncode)

    run("git push")

    print("\n✅ Publié avec succès !\n")


if __name__ == "__main__":
    main()
