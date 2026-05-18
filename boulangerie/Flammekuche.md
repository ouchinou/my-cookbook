# Pâte à Flammekuche Alsacienne

> La véritable recette alsacienne, ultra-rapide et croustillante. Sans levure, elle ne nécessite aucun temps de pousse !

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 10 min (Repos 20 min) | 10 min | <input type="number" id="servings" value="2" min="1" style="width: 50px; font-weight: bold;"> pièces |

## 🛒 Ingrédients
- [ ] <span class="qty" data-base="250">250</span> g de farine T55
- [ ] <span class="qty" data-base="125">125</span> ml d'eau tiède
- [ ] <span class="qty" data-base="3">3</span> cuillères à soupe d'huile de colza ou tournesol
- [ ] <span class="qty" data-base="1">1</span> pincée de sel

## 🥣 Instructions
1. **Le mélange :** Dans un saladier, versez la farine et le sel. Faites un puits, puis ajoutez l'eau tiède et l'huile.
2. **Le pétrissage :** Mélangez à la cuillère puis pétrissez à la main pendant 3 à 5 minutes pour obtenir une pâte homogène et souple. Si la pâte colle, ajoutez un soupçon de farine.
3. **Le repos :** Formez une boule, couvrez-la d'un bol retourné et laissez-la reposer 20 minutes à température ambiante (cela détend le gluten).
4. **L'étalage :** Divisez la pâte selon le nombre de portions. Étalez-la au rouleau à pâtisserie sur un plan de travail fariné afin d'obtenir une pâte de l'épaisseur d'une feuille de papier.

## 💡 Notes & Astuces
- **Garniture traditionnelle :** Mélangez du fromage blanc (faisselle) et de la crème fraîche épaisse, salez, poivrez, ajoutez une pincée de muscade. Parsemez d'oignons émincés et de lardons fumés.
- **Cuisson :** Cuire à four très chaud (250°C-270°C) pendant 8 à 10 minutes, jusqu'à ce que les bords soient colorés et croustillants.

---
[⬅ Retour à l'index](../README.md)

<script>
  const servingInput = document.getElementById('servings');
  const baseServings = 2; // Base pour 2 flammekuches

  servingInput.addEventListener('input', () => {
    const ratio = servingInput.value / baseServings;
    document.querySelectorAll('.qty').forEach(span => {
      const baseValue = parseFloat(span.getAttribute('data-base'));
      let newValue = Math.round((baseValue * ratio) * 10) / 10;
      span.textContent = newValue;
    });
  });
</script>