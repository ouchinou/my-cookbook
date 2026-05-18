# Marinade Indienne Veloutée au Curry

> Le secret des brochettes de poulet "Tandoori" ultra-tendre. L'acide lactique du yaourt décompose les fibres de la viande en douceur, garantissant un résultat fondant sans aucune huile.

| Préparation | Repos conseillé | Portions |
| :--- | :--- | :--- |
| 5 min | 2h à 12h | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. |

## 🛒 Ingrédients
- [ ] <span class="qty" data-base="125">125</span> g de yaourt nature 0% ou de skyr
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe de jus de citron
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe de curry en poudre (ou pâte de tandoori)
- [ ] <span class="qty" data-base="1">1</span> gousse d'ail râpée
- [ ] <span class="qty" data-base="1">1</span> pincée de sel

## 🥣 Instructions
1. **La base :** Dans un grand saladier, fouettez le yaourt (ou le skyr) avec le jus de citron.
2. **L'aromatisation :** Intégrez le curry, l'ail et le sel jusqu'à obtenir une pâte homogène colorée.
3. **L'immersion :** Plongez-y vos dés de blanc de poulet ou de dinde. La viande doit être totalement masquée par le yaourt.
4. **La patience :** Cette marinade gagne à reposer longtemps. Laissez au frais de 2h à toute une nuit. Secouez l'excédent avant de mettre sur la grille.

## 💡 Notes & Astuces
- **Le tips grillade :** À la cuisson sur le Ninja Woodfire, le yaourt va former une petite croûte délicieuse qui retient toute l'eau à l'intérieur de la volaille. Un must pour le mode Grill ou Roast.

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