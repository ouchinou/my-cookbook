# [Nom de la Recette]

> Courte description, anecdote ou origine du plat.

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 15 min | 45 min | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. |

## 🛒 Ingrédients
- [ ] <span class="qty" data-base="250">250</span> g de farine
- [ ] <span class="qty" data-base="3">3</span> œufs
- [ ] <span class="qty" data-base="10">10</span> cl de lait

## 🥣 Instructions
1. **Étape 1 :** Description de la première action à réaliser.
2. **Étape 2 :** Description de la cuisson ou du montage.

## 💡 Notes & Astuces
- Astuce pour remplacer un ingrédient ou améliorer la conservation.

---
[⬅ Retour à l'index](../README.md)

<script>
  const servingInput = document.getElementById('servings');
  const baseServings = 4; // Modifier si la recette de base n'est pas pour 4

  servingInput.addEventListener('input', () => {
    const ratio = servingInput.value / baseServings;
    document.querySelectorAll('.qty').forEach(span => {
      const baseValue = parseFloat(span.getAttribute('data-base'));
      // Calcul avec arrondi à 1 décimale
      let newValue = Math.round((baseValue * ratio) * 10) / 10;
      span.textContent = newValue;
    });
  });
</script>