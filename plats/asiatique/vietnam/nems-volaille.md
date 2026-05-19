# 🥢 Nems à la Volaille

> Variante plus légère des nems traditionnels, avec du poulet haché à la place du porc. Tout aussi croustillants, parfumés au gingembre frais.

| Préparation | Repos | Cuisson | Portions |
| :--- | :--- | :--- | :--- |
| 30 min | 20 min | 15 min | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. (~20 nems) |

## 🛒 Ingrédients

### La farce
- [ ] <span class="qty" data-base="300">300</span> g de blanc de poulet (haché ou mixé)
- [ ] <span class="qty" data-base="50">50</span> g de vermicelles de riz
- [ ] <span class="qty" data-base="15">15</span> g de champignons noirs séchés
- [ ] <span class="qty" data-base="1">1</span> carotte râpée
- [ ] <span class="qty" data-base="2">2</span> oignons verts émincés
- [ ] <span class="qty" data-base="1">1</span> cm de gingembre frais râpé
- [ ] <span class="qty" data-base="2">2</span> gousses d'ail hachées
- [ ] <span class="qty" data-base="1">1</span> œuf
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe de nuoc-mam (sauce poisson)
- [ ] <span class="qty" data-base="1">1</span> cuillère à café d'huile de sésame
- [ ] Poivre noir
- [ ] <span class="qty" data-base="20">20</span> galettes de riz (⌀ 16 cm)
- [ ] Huile de friture

### Sauce nuoc-cham
- [ ] <span class="qty" data-base="3">3</span> cuillères à soupe de nuoc-mam
- [ ] <span class="qty" data-base="2">2</span> cuillères à soupe de sucre
- [ ] <span class="qty" data-base="4">4</span> cuillères à soupe d'eau
- [ ] <span class="qty" data-base="2">2</span> cuillères à soupe de jus de citron vert
- [ ] <span class="qty" data-base="1">1</span> gousse d'ail hachée

## 🥣 Instructions

### 1. Préparer la farce
1. **Réhydrater :** Faire tremper les vermicelles et les champignons dans l'eau chaude **20 min**. Égoutter, essorer et couper grossièrement.
2. **Mixer le poulet :** Si vous utilisez des blancs entiers, les mixer grossièrement (texture hachée, pas pâte lisse).
3. **Mélanger :** Combiner le poulet, les vermicelles, les champignons, la carotte, les oignons verts, le gingembre, l'ail et l'œuf. Assaisonner avec le nuoc-mam, l'huile de sésame et le poivre.

### 2. Rouler les nems
1. **Ramollir les galettes :** Tremper brièvement une galette dans de l'eau tiède (5-10 secondes). Poser à plat.
2. **Garnir :** Déposer 1 cuillère à soupe de farce sur le bas de la galette.
3. **Rouler :** Rabattre les côtés, puis rouler fermement du bas vers le haut.
4. Répéter pour les 20 nems.

### 3. Friture
1. Chauffer l'huile à **170-175 °C**.
2. Frire par 4-5, en retournant régulièrement, **6 à 8 min** jusqu'à dorure uniforme.
3. Égoutter sur du papier absorbant.

### 4. Sauce nuoc-cham
1. Mélanger tous les ingrédients. Goûter et ajuster.

## 💡 Notes & Astuces
- **Poulet entier :** Si vous n'avez pas de hachoir, hacher les blancs au couteau en petits dés fins (donne une meilleure texture qu'un mixeur).
- **Variante canard :** Remplacer le poulet par du magret de canard haché pour une version plus festive.
- **Double friture :** Première friture 160 °C (4 min), repos, puis 180 °C juste avant de servir pour un croustillant parfait.

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
