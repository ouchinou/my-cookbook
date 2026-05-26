"""Module de vérification et correction des recettes du cookbook."""

import os
import re
import sys
import unicodedata
from pathlib import Path

REQUIRED_SECTIONS = ["## 🛒 Ingrédients", "## 🥣 Instructions", "| Préparation |"]


def normalize_name(name: str) -> str:
    """Convertit un nom en version valide : minuscules, sans accents, caractères invalides → '-'."""
    name = name.lower()
    name = unicodedata.normalize("NFD", name)
    name = "".join(c for c in name if unicodedata.category(c) != "Mn")
    name = re.sub(r"[^a-z0-9\-\._]", "-", name)
    name = re.sub(r"-{2,}", "-", name)
    name = name.strip("-")
    return name


def suggest_fixed_path(relative_path: str) -> str:
    """Retourne une version corrigée du chemin relatif."""
    parts = Path(relative_path).parts
    fixed_parts: list[str] = []
    for part in parts:
        if re.match(r"^[a-z0-9\-\._]+$", part):
            fixed_parts.append(part)
        else:
            fixed_parts.append(normalize_name(part))
    return str(Path(*fixed_parts))


def apply_fix(original_path: str, fixed_path: str) -> None:
    """Renomme composant par composant de orig vers fixed (du plus haut vers le plus bas)."""
    orig_parts = list(Path(original_path).parts)
    fixed_parts = list(Path(fixed_path).parts)

    accumulated_orig: list[str] = []
    accumulated_fixed: list[str] = []

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


def _check_file_name(
    relative_path: str,
    errors: list[str],
    nom_errors: list[tuple[str, str]],
) -> None:
    """Vérifie que le nom de fichier et ses dossiers parents sont valides."""
    if not re.match(r"^[a-z0-9\-\._/\\]+$", relative_path):
        errors.append(
            f"NOM : '{relative_path}' contient des caractères invalides"
            " (accents, majuscules, espaces)."
        )
        fixed = suggest_fixed_path(relative_path)
        if fixed != relative_path:
            nom_errors.append((relative_path, fixed))


def _check_file_content(
    path: str,
    errors: list[str],
    link_errors: list[str],
) -> None:
    """Vérifie le contenu d'un fichier recette."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        for section in REQUIRED_SECTIONS:
            if section not in content:
                errors.append(f"TEMPLATE : '{path}' manque la section '{section}'.")
        if not re.search(r"\[.*Retour.*\]\(.*README\.md\)", content):
            errors.append(
                f"RETOUR : '{path}' manque le lien de retour vers l'index"
                " (ex: [⬅ Retour à l'index](../README.md))."
            )
            link_errors.append(path)
    except (OSError, UnicodeDecodeError) as e:
        errors.append(f"LECTURE : Impossible de lire '{path}' ({e})")


def _prompt_and_fix_names(
    nom_errors: list[tuple[str, str]],
    should_fix: bool,
) -> None:
    """Affiche les erreurs de nommage et propose leur correction."""
    print(
        f"\n💡 {len(nom_errors)} fichier(s) avec des noms invalides"
        " peuvent être corrigés automatiquement :"
    )
    for orig, fixed in nom_errors:
        print(f"     {orig}  →  {fixed}")

    if should_fix:
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


def _prompt_and_fix_links(
    link_errors: list[str],
    should_fix: bool,
) -> None:
    """Affiche les erreurs de lien de retour et propose leur correction."""
    print(
        f"\n💡 {len(link_errors)} fichier(s) sans lien de retour"
        " peuvent être corrigés automatiquement :"
    )
    for p in link_errors:
        print(f"     {p}  →  ajout de [⬅ Retour à l'index](../README.md)")

    if should_fix:
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
            print("Aucune correction appliquée.")


def check_recipes(should_fix: bool = False) -> None:
    """Vérifie la conformité de toutes les recettes du cookbook."""
    errors: list[str] = []
    nom_errors: list[tuple[str, str]] = []
    link_errors: list[str] = []

    for root, dirs, files in os.walk("."):
        dirs[:] = [
            d for d in dirs if not d.startswith((".", "assests", "venv", "__pycache__"))
        ]
        for file in files:
            if file.endswith(".md") and file.lower() not in (
                "readme.md",
                "template.md",
            ):
                path = os.path.join(root, file)
                relative_path = os.path.relpath(path, ".")
                _check_file_name(relative_path, errors, nom_errors)
                _check_file_content(path, errors, link_errors)

    if errors:
        print(f"❌ {len(errors)} erreur(s) de validation trouvée(s) :", flush=True)
        for error in errors:
            print(f"  - {error}", flush=True)
        if nom_errors:
            _prompt_and_fix_names(nom_errors, should_fix)
        if link_errors:
            _prompt_and_fix_links(link_errors, should_fix)
        sys.stdout.flush()
        sys.exit(1)
    else:
        print("✅ Toutes les recettes sont conformes !", flush=True)
        sys.stdout.flush()
        sys.exit(0)


def _do_fixes(nom_errors: list[tuple[str, str]]) -> None:
    """Applique les corrections de nommage."""
    fixed_count = 0
    for orig, fixed in nom_errors:
        try:
            apply_fix(orig, fixed)
            print(f"  ✅ {orig}  →  {fixed}")
            fixed_count += 1
        except OSError as e:
            print(f"  ❌ Impossible de renommer '{orig}' : {e}")
    print(
        f"\n✅ {fixed_count}/{len(nom_errors)} fichier(s) corrigé(s)."
        " Relancez le script pour vérifier."
    )


def fix_back_link(path: str) -> None:
    """Ajoute [⬅ Retour à l'index](../README.md) avant le bloc <script> ou en fin de fichier."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    link_line = "[⬅ Retour à l'index](../README.md)"

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


def _do_fix_links(link_errors: list[str]) -> None:
    """Applique les corrections de lien de retour."""
    fixed_count = 0
    for path in link_errors:
        try:
            fix_back_link(path)
            print(f"  ✅ lien de retour ajouté dans '{path}'")
            fixed_count += 1
        except OSError as e:
            print(f"  ❌ Impossible de corriger '{path}' : {e}")
    print(
        f"\n✅ {fixed_count}/{len(link_errors)} fichier(s) corrigé(s)."
        " Relancez le script pour vérifier."
    )


if __name__ == "__main__":
    auto_fix = "--fix" in sys.argv
    check_recipes(should_fix=auto_fix)
