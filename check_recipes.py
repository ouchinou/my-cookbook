import os
import re
import sys


def check_recipes():
    errors = []
    # Sections obligatoires dans votre template
    required_sections = ["## 🛒 Ingrédients", "## 🥣 Instructions", "| Préparation |"]

    for root, dirs, files in os.walk("."):
        # On ignore les dossiers techniques
        dirs[:] = [d for d in dirs if not d.startswith((".", "assets"))]

        for file in files:
            if file.endswith(".md") and file != "README.md":
                path = os.path.join(root, file)

                # 1. Vérification du nom de fichier (Pas d'accents, pas d'espaces)
                if not re.match(r"^[a-z0-9\-\.]+$", file):
                    errors.append(
                        f"NOM : '{file}' contient des accents, majuscules ou espaces."
                    )

                # 2. Vérification du contenu (Template)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                    for section in required_sections:
                        if section not in content:
                            errors.append(
                                f"TEMPLATE : '{file}' manque la section '{section}'."
                            )

    if errors:
        print("❌ Erreurs de validation trouvées :")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)  # Force l'échec de la GitHub Action
    else:
        print("✅ Toutes les recettes respectent les standards !")
        sys.exit(0)


if __name__ == "__main__":
    check_recipes()
