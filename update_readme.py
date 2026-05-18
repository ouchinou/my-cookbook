import os


def generate_readme():
    """Génère le README.md en classant les recettes par dossiers."""
    # Configuration des catégories (Mapping Dossier -> Titre)
    categories = {
        "aperos": "🍸 Apéros & Entrées",
        "plats": "🥘 Plats Résistants",
        "sauces": "🍯 Sauces & Marinades",
        "desserts": "🍰 Desserts Gourmands",
        "divers": "🍽️ Divers & Accompagnements",
        "boulangerie": "🥖 Pâtes & Boulangerie",
        "bbq": "🔥 Recettes pour le BBQ",
    }

    readme_content = "# 📖 Mon Carnet de Recettes\n\n"
    readme_content += "Bienvenue dans mon livre de cuisine automatisé !\n\n"

    # Parcours des catégories définies
    for folder, title in categories.items():
        if os.path.exists(folder):
            # Récupération récursive de tous les fichiers .md
            recipe_files = []
            for root, dirs, files in os.walk(folder):
                for file in sorted(files):
                    if file.endswith(".md"):
                        path = os.path.join(root, file).replace("\\", "/")
                        recipe_files.append(path)

            if recipe_files:
                readme_content += f"## {title}\n"
                for path in sorted(recipe_files):
                    file = os.path.basename(path)
                    # Transformation du nom de fichier en titre lisible
                    display_name = (
                        file.replace(".md", "").replace("-", " ").replace("_", " ").capitalize()
                    )
                    readme_content += f"- [{display_name}]({path})\n"
                readme_content += "\n"

    # Sauvegarde du fichier final
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    print("✅ README.md mis à jour avec toutes les catégories !")


if __name__ == "__main__":
    generate_readme()
