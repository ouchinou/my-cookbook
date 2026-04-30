# 🥣 Sauce Onctueuse Yaourt & Herbes

> Une sauce fraîche et polyvalente, idéale pour accompagner des légumes croquants, des Doritos ou des grillades.

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 10 min | 0 min | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. |

## 🛒 Ingrédients
- [ ] <span class="qty" data-base="1">1</span> pot de crème fraîche (30% MG)
- [ ] <span class="qty" data-base="1">1</span> pot de yaourt grec (ou turc Suzme)
- [ ] <span class="qty" data-base="1">1</span> filet d'huile d'olive
- [ ] <span class="qty" data-base="1">1</span> gousse d'ail hachée
- [ ] Sel, menthe, origan (au goût)

## 🥣 Instructions
1. **Mélange de base :** Dans un bol, mélanger la crème fraîche et le yaourt grec jusqu'à obtenir une texture lisse.
2. **Assaisonnement :** Ajouter l'ail haché, le sel et les herbes (menthe et origan).
3. **Liaison :** Verser un filet d'huile d'olive et mélanger délicatement pour garder l'onctuosité.
4. **Repos :** Laisser reposer au frais au moins 30 minutes avant de servir pour que les arômes se diffusent.

## 💡 Notes & Astuces
- Pour une version encore plus ferme (idéale pour les Doritos), privilégiez le yaourt turc **Suzme** qui est bien égoutté.
- Accompagnement : Carottes, concombres ou bâtonnets de céleri.

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