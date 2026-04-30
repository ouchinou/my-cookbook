import os


def generate_readme():
    # Configuration des catégories basées sur vos noms de dossiers
    categories = {
        "plats": "🥘 Plats Résistants",
        "aperos": "🍸 Apéros & Entrées",
        "desserts": "🍰 Desserts Gourmands",
    }

    readme_content = "# 📖 Mon Carnet de Recettes\n\n"
    readme_content += "Bienvenue dans mon livre de cuisine automatisé ! Les proportions s'adaptent dynamiquement.\n\n"

    # On parcourt chaque dossier défini dans nos catégories
    for folder, title in categories.items():
        if os.path.exists(folder):
            files = [f for f in os.listdir(folder) if f.endswith(".md")]

            if files:
                readme_content += f"## {title}\n"
                for file in sorted(files):
                    # On transforme 'ma-recette.md' en 'Ma recette' pour le titre
                    display_name = (
                        file.replace(".md", "").replace("-", " ").capitalize()
                    )
                    path = f"{folder}/{file}"
                    readme_content += f"- [{display_name}]({path})\n"
                readme_content += "\n"

    # Écriture du fichier
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    print("✅ README.md mis à jour avec catégories !")


if __name__ == "__main__":
    generate_readme()
