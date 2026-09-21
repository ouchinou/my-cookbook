import base64
import json
import subprocess
import sys
from pathlib import Path

import requests

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
RAW_DIR = Path("raw_recipes")
PROCESSED_DIR = Path("processed_images")

OLLAMA_CHAT_URL = "http://localhost:11434/api/chat"
VISION_MODEL = "qwen2.5vl:7b"
TEXT_MODEL = "qwen2.5:7b"

# Liste stricte de tes dossiers de recettes existants
ALLOWED_CATEGORIES = [
    "aperos",
    "entrees",
    "plats",
    "boulangerie_pates",
    "sauces",
    "bbq",
    "desserts",
]


def encode_image(image_path: Path) -> str:
    """Convertit l'image en base64."""
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode("utf-8")


def run_ocr(image_path: Path) -> str:
    """Étape 1 : Extrait le texte brut de la photo via l'API Chat."""
    print(f"\n📸 [1/3] OCR en cours : {image_path.name}...")
    img_b64 = encode_image(image_path)

    payload = {
        "model": VISION_MODEL,
        "messages": [
            {
                "role": "user",
                "content": (
                    "Fais un OCR très précis de cette photo de recette. "
                    "Reconstruis l'intégralité du texte (titre, ingrédients, quantités, instructions)."
                ),
                "images": [img_b64],
            }
        ],
        "stream": False,
    }

    res = requests.post(OLLAMA_CHAT_URL, json=payload)
    res.raise_for_status()

    # Extraction de la réponse depuis la structure de /api/chat
    response_data = res.json()
    return response_data.get("message", {}).get("content", "")


def format_recipe(raw_text: str) -> dict:
    """Étape 2 : Structure la recette au format JSON conforme au template."""
    print("🧠 [2/3] Structuration au format du template Markdown...")

    prompt = f"""
Tu es un assistant culinaire. Transforme le texte brut ci-dessous en un objet JSON strictement valide.

RÈGLES DU JSON :
{{
  "category": "nom_du_dossier",
  "filename": "nom-de-la-recette.md",
  "content": "contenu_markdown_complet"
}}

CRITÈRES STRICTS POUR "content" (OBLIGATOIRES POUR LA VALIDATION) :
1. "category" doit être obligatoirement l'un de ces mots exacts : {ALLOWED_CATEGORIES}.
2. "filename" doit être en minuscules, sans accents, avec des tirets (ex: tarte-aux-pommes.md).
3. Le tableau des temps DOIT contenir exactement la chaîne "| Préparation |" dans son en-tête. Exemple exact :

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 20 min | 30 min | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. |

4. Les sections suivantes sont STRICTEMENT OBLIGATOIRES (respecte les emojis et titres) :
   - ## 🛒 Ingrédients
   - ## 🥣 Instructions
5. Inclus le bloc de séparation "---", le lien de retour "[⬅ Retour à l'index](../README.md)" et le script JavaScript en fin de fichier.

TEMPLATE OBLIGATOIRE À SUIVRE :
# Titre de la Recette
> Courte description résumée

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| XX min | XX min | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. |

## 🛒 Ingrédients
- [ ] <span class="qty" data-base="200">200</span> g de farine

## 🥣 Instructions
1. **Étape :** Instructions...

## 💡 Notes & Astuces
- Astuce...

---
[⬅ Retour à l'index](../README.md)
<script>
const servingInput = document.getElementById('servings');
const baseServings = 4;
servingInput.addEventListener('input', () => {{
  const ratio = servingInput.value / baseServings;
  document.querySelectorAll('.qty').forEach(span => {{
    const baseValue = parseFloat(span.getAttribute('data-base'));
    let newValue = Math.round((baseValue * ratio) * 10) / 10;
    span.textContent = newValue;
  }});
}});
</script>

--- TEXTE BRUT OBTENU PAR OCR ---
{raw_text}
"""

    payload = {
        "model": TEXT_MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
        "format": "json",
        "stream": False,
    }

    res = requests.post(OLLAMA_CHAT_URL, json=payload)
    res.raise_for_status()

    content = res.json().get("message", {}).get("content", "{}")
    return json.loads(content)


def process_all():
    RAW_DIR.mkdir(exist_ok=True)
    PROCESSED_DIR.mkdir(exist_ok=True)

    images = [
        p
        for p in RAW_DIR.glob("*")
        if p.suffix.lower() in [".jpg", ".jpeg", ".png", ".webp"]
    ]

    if not images:
        print("ℹ️ Aucune image trouvée dans le dossier 'raw_recipes/'.")
        return

    for img_path in images:
        # 1. OCR
        raw_text = run_ocr(img_path)

        # 2. Structuration
        data = format_recipe(raw_text)

        category = data.get("category", "plats")
        if category not in ALLOWED_CATEGORIES:
            category = "plats"

        filename = data.get("filename", f"{img_path.stem}.md")
        if not filename.endswith(".md"):
            filename += ".md"

        content = data.get("content", "")

        # Sauvegarde du fichier Markdown
        target_dir = Path(category)
        target_dir.mkdir(exist_ok=True)
        out_file = target_dir / filename

        with open(out_file, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"✅ Recette créée : {out_file}")

        # Déplacement de l'image traitée
        img_path.rename(PROCESSED_DIR / img_path.name)

    # 3. Lancement de la vérification et publication Git
    print("\n🚀 [3/3] Publication automatique via publish.py...")
    subprocess.run([sys.executable, "publish.py", "--fix"])


if __name__ == "__main__":
    process_all()