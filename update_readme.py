import os

# ---------------------------------------------------------------------------
# Configuration des catégories (dossier racine → titre affiché)
# ---------------------------------------------------------------------------
CATEGORIES = {
    "aperos":            "🍸 Apéros & Entrées",
    "entrees":           "🥗 Entrées",
    "plats":             "🥘 Plats",
    "boulangerie_pates": "🥖 Pâtes & Boulangerie",
    "sauces":            "🍯 Sauces, Marinades & Rubs",
    "bbq":               "🔥 BBQ",
    "desserts":          "🍰 Desserts",
}

# Titres affichés (avec emoji) pour tous les sous-dossiers connus
SUBFOLDER_TITLES = {
    # Plats — regroupements géographiques
    "asiatique":   "🌏 Cuisine Asiatique",
    "france":      "🇫🇷 Cuisine Française",
    "mexique":     "🌮 Mexique",
    "tex-mex":     "🌯 Tex-Mex",
    "inde":        "🍛 Inde",
    "autres":      "🍽️ Autres",
    # Régions françaises
    "alsace":      "🥨 Alsace",
    "bourgogne":   "🍷 Bourgogne",
    "bretagne":    "🥞 Bretagne",
    "corse":       "🏝️ Corse",
    "lyon":        "🍽️ Lyon & Rhône-Alpes",
    "normandie":   "🧈 Normandie",
    "nord":        "🧅 Nord & Hauts-de-France",
    "pays-basque": "🌶️ Pays Basque",
    "perigord":    "🦆 Périgord & Dordogne",
    "provence":    "🌿 Provence & Côte d'Azur",
    "savoie":      "🏔️ Savoie & Alpes",
    # Cuisines asiatiques
    "chine":       "🥟 Chine",
    "coree":       "🥢 Corée du Sud",
    "indonesie":   "🍜 Indonésie",
    "japon":       "🍣 Japon",
    "thai":        "🌶️ Thaïlande",
    "vietnam":     "🫕 Vietnam",
    # BBQ
    "grill":       "🔥 Grill",
    "roast":       "🍗 Rôtisserie",
    "smoke":       "💨 Fumage",
    # Sauces
    "marinades":   "🫙 Marinades",
    "rubs":        "🧂 Rubs & Épices",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_folder_title(folder_name):
    """Retourne le titre d'un sous-dossier (avec emoji si connu)."""
    return SUBFOLDER_TITLES.get(
        folder_name,
        folder_name.replace("-", " ").replace("_", " ").title(),
    )


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


def count_recipes(folder):
    """Compte le nombre total de recettes (.md hors README) dans un dossier."""
    total = 0
    for root, dirs, files in os.walk(folder):
        dirs[:] = [d for d in dirs if not d.startswith((".", "__"))]
        total += sum(
            1 for f in files if f.endswith(".md") and f.lower() != "readme.md"
        )
    return total


# ---------------------------------------------------------------------------
# Génération récursive des README
# ---------------------------------------------------------------------------

def generate_folder_readme(folder, title, depth=0):
    """
    Génère le README.md d'un dossier, puis appelle récursivement ses sous-dossiers.

    - Dossier avec sous-dossiers → tableau de navigation (catégorie + nb recettes)
    - Dossier feuille            → liste de recettes (ou message "aucune recette")
    """
    try:
        entries = sorted(os.listdir(folder))
    except FileNotFoundError:
        return

    subfolders = [
        d for d in entries
        if os.path.isdir(os.path.join(folder, d)) and not d.startswith((".", "__"))
    ]
    direct_recipes = [
        (os.path.join(folder, f), get_recipe_title(os.path.join(folder, f)))
        for f in entries
        if (
            os.path.isfile(os.path.join(folder, f))
            and f.endswith(".md")
            and f.lower() != "readme.md"
        )
    ]

    back_label = "Retour à l'accueil" if depth == 0 else "Retour"
    lines = [f"# {title}\n"]

    if subfolders:
        # ── Dossier intermédiaire : tableau des sous-catégories ───────────
        lines += ["| Catégorie | Recettes |", "| :--- | :---: |"]
        for sub in subfolders:
            sub_title = get_folder_title(sub)
            n = count_recipes(os.path.join(folder, sub))
            lines.append(f"| [{sub_title}]({sub}/) | {n} |")

        if direct_recipes:  # recettes rangées directement (cas mixte rare)
            lines += ["\n## Recettes générales\n"]
            for fp, rt in direct_recipes:
                lines.append(f"- [{rt}]({os.path.basename(fp)})")
    else:
        # ── Dossier feuille : liste de recettes ───────────────────────────
        if direct_recipes:
            for fp, rt in direct_recipes:
                lines.append(f"- [{rt}]({os.path.basename(fp)})")
        else:
            lines.append("*Aucune recette pour l'instant.*")

    lines += ["", "---", f"[⬅ {back_label}](../)", ""]

    readme_path = os.path.join(folder, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  📄 {readme_path}  ({count_recipes(folder)} recettes)")

    # ── Récursion ─────────────────────────────────────────────────────────
    for sub in subfolders:
        generate_folder_readme(
            os.path.join(folder, sub),
            get_folder_title(sub),
            depth + 1,
        )


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
            n = count_recipes(folder)
            if n > 0:
                lines.append(f"| [{title}]({folder}/) | {n} |")
    lines.append("")
    with open("README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("  📄 README.md  (index principal)")


def generate_all():
    print("🔄 Génération des index...")
    generate_main_readme()
    for folder, title in CATEGORIES.items():
        if os.path.exists(folder):
            generate_folder_readme(folder, title, depth=0)
    print("✅ Tous les index sont à jour !")


if __name__ == "__main__":
    generate_all()
