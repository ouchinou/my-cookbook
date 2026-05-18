# Marinade Mexicaine Citron Vert & Coriandre

> Une marinade pleine de peps, idéale pour relever des hauts de cuisse de poulet, des crevettes ou des lanières de bœuf pour fajitas au grill. Zéro matière grasse ajoutée !

| Préparation | Repos conseillé | Portions |
| :--- | :--- | :--- |
| 5 min | 1h à 3h | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. |

## 🛒 Ingrédients
- [ ] <span class="qty" data-base="2">2</span> citrons verts (jus)
- [ ] <span class="qty" data-base="1">1</span> cuillère à café de cumin en poudre
- [ ] <span class="qty" data-base="1">1</span> cuillère à café de paprika fumé (Pimentón)
- [ ] <span class="qty" data-base="1">1</span> gousse d'ail pressée
- [ ] <span class="qty" data-base="0.5">0.5</span> botte de coriandre fraîche ciselée

## 🥣 Instructions
1. **Le pressage :** Pressez les citrons verts dans votre plat de marinade.
2. **Les épices :** Intégrez le cumin, le paprika fumé (qui rappelle la fumée du Woodfire), l'ail et la coriandre ciselée.
3. **Le massage :** Badigeonnez bien vos morceaux de viande ou de crustacés avec ce mélange puissant.
4. **Le repos :** Laissez reposer 1 heure au frais avant de saisir à haute température (Mode Grill HI).

## 💡 Notes & Astuces
- Pour les amateurs de piquant, vous pouvez ajouter quelques rondelles de piment jalapeño frais ou une pincée de piment de Cayenne dans la préparation.

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