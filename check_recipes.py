import os
import re
import sys


def check_recipes():
    errors = []
    # Sections obligatoires
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
                    errors.append(
                        f"NOM : '{path}' contient des caractères invalides (accents, majuscules, espaces)."
                    )

                # 2. Vérification du contenu
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                        for section in required_sections:
                            if section not in content:
                                errors.append(
                                    f"TEMPLATE : '{path}' manque la section '{section}'."
                                )
                except Exception as e:
                    errors.append(f"LECTURE : Impossible de lire '{path}' ({e})")

    if errors:
        print(f"❌ {len(errors)} erreur(s) de validation trouvée(s) :", flush=True)
        for error in errors:
            print(f"  - {error}", flush=True)
        sys.stdout.flush()
        sys.exit(1)
    else:
        print("✅ Toutes les recettes sont conformes !", flush=True)
        sys.stdout.flush()
        sys.exit(0)


if __name__ == "__main__":
    check_recipes()
