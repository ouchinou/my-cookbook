# 🥢 Nems au Porc

> Les classiques de la cuisine vietnamienne : des rouleaux frits croustillants, farcis au porc, aux vermicelles et aux champignons noirs. À tremper dans la sauce nuoc-cham.

| Préparation | Repos | Cuisson | Portions |
| :--- | :--- | :--- | :--- |
| 30 min | 20 min | 15 min | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. (~20 nems) |

## 🛒 Ingrédients

### La farce
- [ ] <span class="qty" data-base="300">300</span> g de porc haché (épaule ou mélange 50/50 porc/veau)
- [ ] <span class="qty" data-base="50">50</span> g de vermicelles de riz
- [ ] <span class="qty" data-base="15">15</span> g de champignons noirs séchés
- [ ] <span class="qty" data-base="1">1</span> carotte râpée
- [ ] <span class="qty" data-base="0.5">0.5</span> oignon (finement émincé)
- [ ] <span class="qty" data-base="2">2</span> gousses d'ail hachées
- [ ] <span class="qty" data-base="1">1</span> œuf
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe de nuoc-mam (sauce poisson)
- [ ] Poivre noir
- [ ] <span class="qty" data-base="20">20</span> galettes de riz (⌀ 16 cm)
- [ ] Huile de friture

### Sauce nuoc-cham
- [ ] <span class="qty" data-base="3">3</span> cuillères à soupe de nuoc-mam
- [ ] <span class="qty" data-base="2">2</span> cuillères à soupe de sucre
- [ ] <span class="qty" data-base="4">4</span> cuillères à soupe d'eau
- [ ] <span class="qty" data-base="2">2</span> cuillères à soupe de jus de citron vert
- [ ] <span class="qty" data-base="1">1</span> gousse d'ail hachée
- [ ] <span class="qty" data-base="0.5">0.5</span> piment rouge (facultatif)

## 🥣 Instructions

### 1. Préparer la farce
1. **Réhydrater :** Faire tremper les vermicelles et les champignons dans l'eau chaude **20 min**. Égoutter, essorer et couper grossièrement.
2. **Mélanger :** Combiner le porc haché, les vermicelles, les champignons, la carotte, l'oignon, l'ail et l'œuf. Assaisonner avec le nuoc-mam et le poivre. Mélanger bien.

### 2. Rouler les nems
1. **Ramollir les galettes :** Tremper brièvement une galette de riz dans de l'eau tiède (5-10 secondes) jusqu'à ce qu'elle devienne souple. Poser à plat.
2. **Garnir :** Déposer 1 cuillère à soupe de farce sur le bas de la galette.
3. **Rouler :** Rabattre les côtés sur la farce, puis rouler fermement du bas vers le haut.
4. Répéter pour les 20 nems.

### 3. Friture
1. Chauffer l'huile à **170-175 °C** (pas trop fort pour éviter que les galettes brûlent avant la cuisson de la farce).
2. Plonger les nems par 4-5, les retourner régulièrement, frire **6 à 8 min** jusqu'à coloration dorée uniforme.
3. Égoutter sur du papier absorbant.

### 4. Sauce nuoc-cham
1. Mélanger tous les ingrédients. Goûter et ajuster le sucre/citron selon votre goût.

## 💡 Notes & Astuces
- **Double friture :** Pour des nems très croustillants, faire une première friture à 160 °C (4 min), laisser refroidir, puis une seconde à 180 °C juste avant de servir.
- **Congélation :** Se congèlent très bien crus. Frire directement sans décongeler en rajoutant 2-3 min.
- **Service :** Servir avec de la salade, des feuilles de menthe et enrouler dans une feuille de laitue.

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
