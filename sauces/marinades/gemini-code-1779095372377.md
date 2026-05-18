# Marinade Teriyaki Allégée

> Le grand classique asiatique revisité en version low-fat. Parfaite pour le saumon au fumoir (Smoke), le bœuf au grill ou le poulet. Elle apporte une magnifique caramélisation à la cuisson.

| Préparation | Repos conseillé | Portions |
| :--- | :--- | :--- |
| 5 min | 1h à 4h | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. |

## 🛒 Ingrédients
- [ ] <span class="qty" data-base="8">8</span> cuillères à soupe de sauce soja allégée en sel
- [ ] <span class="qty" data-base="2">2</span> cuillères à soupe de miel (ou sirop d'érable)
- [ ] <span class="qty" data-base="1">1</span> cuillère à café de gingembre frais râpé
- [ ] <span class="qty" data-base="1">1</span> gousse d'ail écrasée
- [ ] <span class="qty" data-base="1">1</span> cuillère à café d'huile de sésame (pour le parfum)

## 🥣 Instructions
1. **Le mélange :** Dans un bol, délayez le miel dans la sauce soja.
2. **Les aromates :** Ajoutez l'ail, le gingembre râpé et l'huile de sésame. Mélangez bien.
3. **L'enrobage :** Versez sur votre viande ou poisson (idéal avec des pavés de saumon ou des blancs de poulet coupés en dés pour brochettes).
4. **Le repos :** Laissez mariner au réfrigérateur pendant au moins 1 heure.

## 💡 Notes & Astuces
- **Anti-gaspillage :** Vous pouvez récupérer le reste de la marinade (n'ayant pas touché la viande crue ou bouillie au préalable) et la faire réduire 3 minutes à la casserole pour obtenir une sauce nappante.

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