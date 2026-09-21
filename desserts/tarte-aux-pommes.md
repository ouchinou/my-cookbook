# Tarte aux pommes
> 45 min • 6 personnes

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 45 min | 30 min | <input type="number" id="servings" value="6" min="1" style="width: 50px; font-weight: bold;"> pers. |

## 🛒 Ingrédients
- [ ] 1 pâte brisée
- [ ] 3 pommes
- [ ] 30g de sucre
- [ ] 20g de beurre
- [ ] 300g de compote (à faire maison si vous avez le temps)

## 🥣 Instructions
1. **Étape :** Préchauffez à 200°C. Disposez la pâte dans le moule et piquez le fond avec une fourchette.
2. **Étape :** Épluchez les pommes et coupez-elles en tranches d'environ 3 mm d'épaisseur.
3. **Étape :** Disposez une couche de compote de pommes sur le fond de tarte.
4. **Étape :** Ajoutez les pommes et quelques noix de beurre.
5. **Étape :** Saupoudrez de sucre roux.
6. **Étape :** Enfournez pour 30 minutes. C'est prêt !

## 💡 Notes & Astuces
- Astuce : Utilisez une compote de pommes fraîches pour un goût encore plus authentique.
---
[⬅ Retour à l'index](../README.md)
<script>
const servingInput = document.getElementById('servings');
const baseServings = 6;
servingInput.addEventListener('input', () => {
  const ratio = servingInput.value / baseServings;
  document.querySelectorAll('.qty').forEach(span => {
    const baseValue = parseFloat(span.getAttribute('data-base'));
    let newValue = Math.round((baseValue * ratio) * 10) / 10;
    span.textContent = newValue;
  });
});
</script>