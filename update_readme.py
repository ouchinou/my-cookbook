import os


def generate_readme():
    """Génère le README.md en classant les recettes par dossiers."""
    # Configuration des catégories (Mapping Dossier -> Titre)
    categories = {
        "aperos": "🍸 Apéros & Entrées",
        "plats": "🥘 Plats Résistants",
        "sauces": "🍯 Sauces & Marinades",
        "desserts": "🍰 Desserts Gourmands",
    }

    readme_content = "# 📖 Mon Carnet de Recettes\n\n"
    readme_content += "Bienvenue dans mon livre de cuisine automatisé !\n\n"

    # Parcours des catégories définies
    for folder, title in categories.items():
        if os.path.exists(folder):
            # Récupération et tri des fichiers .md
            files = [f for f in os.listdir(folder) if f.endswith(".md")]

            if files:
                readme_content += f"## {title}\n"
                for file in sorted(files):
                    # Transformation du nom de fichier en titre lisible
                    display_name = (
                        file.replace(".md", "").replace("-", " ").capitalize()
                    )
                    path = f"{folder}/{file}"
                    readme_content += f"- [{display_name}]({path})\n"
                readme_content += "\n"

    # Sauvegarde du fichier final
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    print("✅ README.md mis à jour avec la catégorie Sauces !")


if __name__ == "__main__":
    generate_readme()
