import os

# ---------------------------------------------------------------------------
# Configuration des catégories  (dossier → titre affiché)
# ---------------------------------------------------------------------------
CATEGORIES = {
    "aperos": "🍸 Apéros & Entrées",
    "entrees": "🥗 Entrées",
    "plats": "🥘 Plats",
    "boulangerie_pates": "🥖 Pâtes & Boulangerie",
    "sauces": "🍯 Sauces, Marinades & Rubs",
    "bbq": "🔥 BBQ",
    "desserts": "🍰 Desserts",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def get_recipe_title(filepath):
    """Extrait le titre H1 du fichier markdown ; fallback sur le nom de fichier."""
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


def collect_recipes(folder):
    """Retourne un dict {sous-dossier_relatif: [(filepath, titre)]} trié."""
    grouped = {}
    for root, dirs, files in os.walk(folder):
        dirs[:] = sorted(d for d in dirs if not d.startswith((".", "__")))
        md_files = sorted(
            f for f in files if f.endswith(".md") and f.lower() != "readme.md"
        )
        if md_files:
            rel = os.path.relpath(root, folder)
            key = "." if rel == "." else rel
            grouped.setdefault(key, [])
            for f in md_files:
                fp = os.path.join(root, f)
                grouped[key].append((fp, get_recipe_title(fp)))
    return grouped


def count_recipes(folder):
    """Compte le nombre total de recettes (.md hors README) dans un dossier."""
    total = 0
    for root, dirs, files in os.walk(folder):
        dirs[:] = [d for d in dirs if not d.startswith((".", "__"))]
        total += sum(1 for f in files if f.endswith(".md") and f.lower() != "readme.md")
    return total


def subfolder_label(path):
    """Transforme un chemin de sous-dossier en libellé lisible."""
    return (
        path.replace("\\", "/")
        .replace("/", " › ")
        .replace("-", " ")
        .replace("_", " ")
        .title()
    )


# ---------------------------------------------------------------------------
# Génération
# ---------------------------------------------------------------------------


def generate_category_readme(folder, title):
    """Génère le README.md d'index d'une catégorie."""
    grouped = collect_recipes(folder)
    if not grouped:
        return

    lines = [f"# {title}\n"]

    for subfolder in sorted(grouped.keys()):
        recipes = grouped[subfolder]
        if subfolder != ".":
            lines.append(f"\n## {subfolder_label(subfolder)}\n")
        for filepath, recipe_title in recipes:
            rel_path = os.path.relpath(filepath, folder).replace("\\", "/")
            lines.append(f"- [{recipe_title}]({rel_path})")

    lines += ["", "---", "[⬅ Retour à l'accueil](../)", ""]

    readme_path = os.path.join(folder, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  📄 {readme_path}  ({count_recipes(folder)} recettes)")


def generate_main_readme():
    """Génère le README.md principal : tableau de catégories avec compteurs."""
    lines = [
        "# 📖 Mon Carnet de Recettes\n",
        "Bienvenue dans mon livre de cuisine !\n",
        "| Catégorie | Recettes |",
        "| :--- | :---: |",
    ]

    for folder, title in CATEGORIES.items():
        if os.path.exists(folder):
            count = count_recipes(folder)
            if count > 0:
                lines.append(f"| [{title}]({folder}/) | {count} |")

    lines.append("")
    with open("README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("  📄 README.md  (index principal)")


def generate_all():
    print("🔄 Génération des index...")
    generate_main_readme()
    for folder, title in CATEGORIES.items():
        if os.path.exists(folder):
            generate_category_readme(folder, title)
    print("✅ Tous les index sont à jour !")


if __name__ == "__main__":
    generate_all()
