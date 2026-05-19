# 🐟 Accras de Morrue

> Beignets croustillants originaires des Antilles, incontournables de l'apéro créole. La morue est dessalée puis mêlée à une pâte légère parfumée au piment et à la ciboulette.

| Préparation | Repos | Cuisson | Portions |
| :--- | :--- | :--- | :--- |
| 20 min | 12 h | 15 min | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. |

## 🛒 Ingrédients

### La pâte
- [ ] <span class="qty" data-base="300">300</span> g de morue salée (filet)
- [ ] <span class="qty" data-base="150">150</span> g de farine
- [ ] <span class="qty" data-base="2">2</span> œufs
- [ ] <span class="qty" data-base="10">10</span> cl de lait
- [ ] <span class="qty" data-base="0.5">0.5</span> sachet de levure chimique
- [ ] <span class="qty" data-base="1">1</span> piment antillais (ajuster selon tolérance)
- [ ] <span class="qty" data-base="3">3</span> branches de ciboulette
- [ ] <span class="qty" data-base="2">2</span> gousses d'ail
- [ ] <span class="qty" data-base="0.5">0.5</span> oignon blanc
- [ ] Sel, poivre
- [ ] Huile de friture

## 🥣 Instructions

### 1. Dessalage (J-1)
1. **Trempage :** Mettre la morue dans un grand récipient d'eau froide. Changer l'eau **3 à 4 fois** sur 12 heures (ou toute une nuit).
2. **Test :** Goûter un petit morceau de morue cru — il doit être légèrement salé, pas fort.

### 2. Préparation de la farce
1. Égoutter et émietter la morue finement à la fourchette en retirant les arêtes et la peau.
2. Émincer finement l'ail, l'oignon, la ciboulette et le piment (retirer les graines pour doser le piquant).
3. Mélanger la morue émiettée avec les herbes et aromates.

### 3. La pâte
1. Dans un saladier, mélanger la farine et la levure.
2. Faire un puits, ajouter les œufs battus et le lait progressivement en fouettant.
3. Incorporer le mélange morue-herbes. La pâte doit être épaisse (tenir à la cuillère).
4. Saler très légèrement (la morue est déjà salée) et poivrer.

### 4. Friture
1. Chauffer l'huile à **180 °C**.
2. Former des boulettes à la cuillère à soupe et les plonger délicatement dans l'huile.
3. Frire **3 à 4 min** en retournant jusqu'à coloration bien dorée.
4. Égoutter sur du papier absorbant et servir chaud.

## 💡 Notes & Astuces
- **Piment :** Retirer totalement les graines pour des accras doux, garder une partie pour plus de piquant.
- **Réchauffage :** Se réchauffent très bien au four à 180 °C pendant 5 min (redeviennent croustillants).
- **Variante :** Ajouter du thym ou du persil plat pour plus de fraîcheur.

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
