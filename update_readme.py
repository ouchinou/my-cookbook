import os


def generate_readme():
    content = "# 📖 Mon Carnet de Recettes\n\n"
    content += "Bienvenue dans mon livre de cuisine automatisé !\n\n"
    
    # Dossiers à ignorer
    ignore_dirs = ['.git', '.github', 'assets']
    
    # Parcours des dossiers
    for root, dirs, files in sorted(os.walk('.')):
        # On nettoie les dossiers à ignorer
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        
        # On ne traite que les sous-dossiers qui contiennent des fichiers .md
        category = os.path.basename(root)
        if category and category != '.':
            recipes = [f for f in files if f.endswith('.md') and f != 'README.md']
            
            if recipes:
                content += f"## {category.capitalize()}\n"
                for recipe in sorted(recipes):
                    # Création du nom lisible (on enlève .md et les tirets)
                    name = recipe.replace('.md', '').replace('-', ' ').capitalize()
                    path = os.path.join(root, recipe).replace('\\', '/')
                    content += f"* [{name}]({path})\n"
                content += "\n"

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    generate_readme()