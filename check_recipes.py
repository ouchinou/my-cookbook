import os
import re
import sys
import unicodedata
from pathlib import Path


def normalize_name(name):
    """Convertit un nom en version valide : minuscules, sans accents, caractères invalides → '-'."""
    name = name.lower()
    name = unicodedata.normalize("NFD", name)
    name = "".join(c for c in name if unicodedata.category(c) != "Mn")
    name = re.sub(r"[^a-z0-9\-\._]", "-", name)
    name = re.sub(r"-{2,}", "-", name)
    name = name.strip("-")
    return name


def suggest_fixed_path(relative_path):
    """Retourne une version corrigée du chemin relatif."""
    parts = Path(relative_path).parts
    fixed_parts = []
    for part in parts:
        if re.match(r"^[a-z0-9\-\._]+$", part):
            fixed_parts.append(part)
        else:
            fixed_parts.append(normalize_name(part))
    return str(Path(*fixed_parts))


def apply_fix(original_path, fixed_path):
    """Renomme composant par composant de orig vers fixed (du plus haut vers le plus bas)."""
    orig_parts = list(Path(original_path).parts)
    fixed_parts = list(Path(fixed_path).parts)

    accumulated_orig = []
    accumulated_fixed = []

    for op, fp in zip(orig_parts, fixed_parts):
        accumulated_orig.append(op)
        accumulated_fixed.append(fp)

        if op != fp:
            src = Path(*accumulated_orig)
            dst = Path(*accumulated_fixed)
            if src.exists():
                # Sur Windows (insensible à la casse), un renommage purement en minuscules
                # nécessite un passage par un nom temporaire pour forcer le changement.
                if str(src).lower() == str(dst).lower():
                    tmp = src.parent / (src.name + ".__tmp__")
                    src.rename(tmp)
                    tmp.rename(dst)
                elif not dst.exists():
                    src.rename(dst)
            accumulated_orig[-1] = fp  # mise à jour pour les composants suivants


def check_recipes(auto_fix=False):
    errors = []
    nom_errors = []  # liste de (original_path, fixed_path)
    link_errors = []  # liste de chemins manquant le lien de retour

    required_sections = ["## 🛒 Ingrédients", "## 🥣 Instructions", "| Préparation |"]

    for root, dirs, files in os.walk("."):
        # On ignore les dossiers techniques et les assets
        dirs[:] = [
            d for d in dirs if not d.startswith((".", "assests", "venv", "__pycache__"))
        ]

        for file in files:
            # On ne check que les fichiers Markdown qui ne sont pas le README principal ni le template
            if file.endswith(".md") and file.lower() not in (
                "readme.md",
                "template.md",
            ):
                path = os.path.join(root, file)

                # 1. Vérification du nom du fichier ET des dossiers parents
                relative_path = os.path.relpath(path, ".")
                if not re.match(r"^[a-z0-9\-\._/\\]+$", relative_path):
                    fixed = suggest_fixed_path(relative_path)
                    errors.append(
                        f"NOM : '{relative_path}' contient des caractères invalides (accents, majuscules, espaces)."
                    )
                    if fixed != relative_path:
                        nom_errors.append((relative_path, fixed))

                # 2. Vérification du contenu
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                        for section in required_sections:
                            if section not in content:
                                errors.append(
                                    f"TEMPLATE : '{path}' manque la section '{section}'."
                                )
                        if not re.search(r"\[.*Retour.*\]\(.*README\.md\)", content):
                            errors.append(
                                f"RETOUR : '{path}' manque le lien de retour vers l'index (ex: [⬅ Retour à l'index](../README.md))."
                            )
                            link_errors.append(path)
                except Exception as e:
                    errors.append(f"LECTURE : Impossible de lire '{path}' ({e})")

    if errors:
        print(f"❌ {len(errors)} erreur(s) de validation trouvée(s) :", flush=True)
        for error in errors:
            print(f"  - {error}", flush=True)

        if nom_errors:
            print(
                f"\n💡 {len(nom_errors)} fichier(s) avec des noms invalides peuvent être corrigés automatiquement :"
            )
            for orig, fixed in nom_errors:
                print(f"     {orig}  →  {fixed}")

            if auto_fix:
                _do_fixes(nom_errors)
            else:
                print(
                    "\nVoulez-vous corriger ces noms automatiquement ? [o/n] : ",
                    end="",
                    flush=True,
                )
                answer = input().strip().lower()
                if answer in ("o", "oui", "y", "yes"):
                    _do_fixes(nom_errors)
                else:
                    print("Aucune correction appliquée.")
        if link_errors:
            print(
                f"\n\ud83d\udca1 {len(link_errors)} fichier(s) sans lien de retour peuvent \u00eatre corrig\u00e9s automatiquement :"
            )
            for p in link_errors:
                print(
                    f"     {p}  \u2192  ajout de [\u2b05 Retour \u00e0 l'index](../README.md)"
                )

            if auto_fix:
                _do_fix_links(link_errors)
            else:
                print(
                    "\nVoulez-vous ajouter le lien de retour automatiquement ? [o/n] : ",
                    end="",
                    flush=True,
                )
                answer = input().strip().lower()
                if answer in ("o", "oui", "y", "yes"):
                    _do_fix_links(link_errors)
                else:
                    print("Aucune correction appliqu\u00e9e.")
        sys.stdout.flush()
        sys.exit(1)
    else:
        print("✅ Toutes les recettes sont conformes !", flush=True)
        sys.stdout.flush()
        sys.exit(0)


def _do_fixes(nom_errors):
    fixed_count = 0
    for orig, fixed in nom_errors:
        try:
            apply_fix(orig, fixed)
            print(f"  ✅ {orig}  →  {fixed}")
            fixed_count += 1
        except Exception as e:
            print(f"  ❌ Impossible de renommer '{orig}' : {e}")
    print(
        f"\n✅ {fixed_count}/{len(nom_errors)} fichier(s) corrigé(s). Relancez le script pour vérifier."
    )


def fix_back_link(path):
    """Ajoute [\u2b05 Retour \u00e0 l'index](../README.md) avant le bloc <script> ou en fin de fichier."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    link_line = "[\u2b05 Retour \u00e0 l'index](../README.md)"

    if "<script>" in content:
        idx = content.index("<script>")
        before = content[:idx].rstrip()
        after = content[idx:]
        if before.endswith("---"):
            before += "\n" + link_line + "\n\n"
        else:
            before += "\n\n---\n" + link_line + "\n\n"
        content = before + after
    else:
        content = content.rstrip()
        if content.endswith("---"):
            content += "\n" + link_line + "\n"
        else:
            content += "\n\n---\n" + link_line + "\n"

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def _do_fix_links(link_errors):
    fixed_count = 0
    for path in link_errors:
        try:
            fix_back_link(path)
            print(f"  \u2705 lien de retour ajout\u00e9 dans '{path}'")
            fixed_count += 1
        except Exception as e:
            print(f"  \u274c Impossible de corriger '{path}' : {e}")
    print(
        f"\n\u2705 {fixed_count}/{len(link_errors)} fichier(s) corrig\u00e9(s). Relancez le script pour v\u00e9rifier."
    )


if __name__ == "__main__":
    auto_fix = "--fix" in sys.argv
    check_recipes(auto_fix=auto_fix)
