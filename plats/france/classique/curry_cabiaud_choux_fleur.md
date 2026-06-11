# Curry de Cabillaud au Chou-Fleur et Lait de Coco
> Un plat savoureux et onctueux alliant la finesse du cabillaud à la douceur du lait de coco, relevé par un mélange d'épices et une pointe de soja.
| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 20 min | 40 min | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. |
## 🛒 Ingrédients
- [ ] <span class="qty" data-base="600">600</span> g de cabillaud
- [ ] <span class="qty" data-base="750">750</span> g de chou-fleur
- [ ] <span class="qty" data-base="1">1</span> grande brique de lait de coco (400ml)
- [ ] <span class="qty" data-base="2">2</span> oignons
- [ ] <span class="qty" data-base="3">3</span> gousses d'ail
- [ ] <span class="qty" data-base="1">1</span> sachet de mélange épices (curry, paprika, cumin, gingembre, curcuma, coriandre)
- [ ] <span class="qty" data-base="20">20</span> ml de sauce soja salée
- [ ] <span class="qty" data-base="15">15</span> ml de sauce soja sucrée
## 🥣 Instructions
1. **Préparation :** Laver et couper le chou-fleur en fleurettes. Émincer les oignons et hacher l'ail. Couper le cabillaud en gros morceaux.
2. **Cuisson des aromates :** Faire revenir les oignons et l'ail dans une sauteuse avec un peu d'huile jusqu'à ce qu'ils soient tendres, puis ajouter le mélange d'épices pour libérer leurs arômes.
3. **Mijotage :** Verser le lait de coco et ajouter les fleurettes de chou-fleur. Laisser mijoter à feu moyen jusqu'à ce que le chou soit tendre.
4. **Cuisson du poisson :** Ajouter les morceaux de cabillaud dans la sauce pour les 10 dernières minutes de cuisson.
5. **Finition :** Juste avant de servir, ajouter la sauce soja salée et la sauce soja sucrée. Rectifier le sel et le poivre.
## 💡 Notes & Astuces
- Pour un goût plus authentique, vous pouvez ajouter une pincée de piment en poudre selon votre tolérance au piquant.
- Le mélange de sojas (salé/sucré) apporte une profondeur "umami" qui équilibre parfaitement le gras du lait de coco.
---
[⬅ Retour à l'index](../README.md)
<script>
const servingInput = document.getElementById('servings');
const baseServings = 4; 
servingInput.addEventListener('input', () => {
const ratio = servingInput.value / baseServings;
document.querySelectorAll('.qty').forEach(span => {
const baseValue = parseFloat(span.getAttribute('data-base'));
let newValue = Math.round((baseValue * ratio) * 10) / 10;
span.textContent = newValue;
});
});
</script>