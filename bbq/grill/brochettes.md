# Le Festival de Brochettes au Grill

> Une recette déclinable en 3 versions (poulet au curry, saumon teriyaki, crevettes ail & citron). Le mode Grill permet de saisir les brochettes rapidement sans dessécher l'intérieur.

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 20 min | 8 min | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. |

## 🛒 Ingrédients
- [ ] <span class="qty" data-base="600">600</span> g de protéines au choix (Blancs de poulet, pavés de saumon ou grosses crevettes décortiquées)
- [ ] <span class="qty" data-base="2">2</span> cuillères à soupe d'huile d'olive (ou huile de sésame pour le saumon)
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe d'épices au choix (Curry pour le poulet, Sauce Teriyaki pour le saumon, Ail & Aneth pour les crevettes)
- [ ] <span class="qty" data-base="1">1</span> poivron coupé en dés (pour le montage)

## 🥣 Instructions
1. **La découpe :** Coupez vos protéines (viande ou poisson) en cubes réguliers d'environ 3 cm. 
2. **L'assaisonnement :** Dans un récipient, mélangez les cubes avec l'huile et les épices choisies. Laissez reposer 15 minutes.
3. **Le montage :** Enfilez les cubes sur des pics à brochette en alternant avec les morceaux de poivron.
4. **La configuration :** Sélectionnez la fonction **GRILL**, réglez la température sur **MED (Moyenne)** pour le poisson/crevettes ou **HI (Élevée)** pour le poulet. Réglez le temps sur 10 minutes et lancez le préchauffage.
5. **La cuisson :** Au signal *ADD FOOD*, déposez les brochettes. Laissez cuire couvercle fermé pendant 4 minutes pour les crevettes/poissons (retourner à mi-cuisson) et 7 à 8 minutes pour le poulet en les retournant à mi-parcours pour s'assurer que la volaille soit bien cuite.

## 💡 Notes & Astuces
- Si vous utilisez des pics en bois, trempez-les dans l'eau pendant 30 minutes avant le montage pour éviter qu'ils ne brûlent sur la grille.

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