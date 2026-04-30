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
            d for d in dirs if not d.startswith((".", "assets", "venv", "__pycache__"))
        ]

        for file in files:
            # On ne check que les fichiers Markdown qui ne sont pas le README principal
            if file.endswith(".md") and file.lower() != "readme.md":
                path = os.path.join(root, file)

                # 1. Vérification du nom (Ajout de l'underscore _ dans la regex)
                if not re.match(r"^[a-z0-9\-\._]+$", file):
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
        print(f"❌ {len(errors)} erreur(s) de validation trouvée(s) :")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)
    else:
        print("✅ Toutes les recettes sont conformes !")
        sys.exit(0)


if __name__ == "__main__":
    check_recipes()
