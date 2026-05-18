# La Véritable Flamiche au Maroilles

> Originaire de la région du Nord, cette tarte salée utilise une pâte levée briochée, moelleuse à souhait, sur laquelle fond le Maroilles, ce fromage au caractère affirmé mais d'une douceur incroyable une fois cuit.

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 20 min (Repos 1h30) | 25 min | <input type="number" id="servings" value="6" min="1" style="width: 50px; font-weight: bold;"> pers. |

## 🛒 Ingrédients
- [ ] <span class="qty" data-base="250">250</span> g de farine T45 ou T55
- [ ] <span class="qty" data-base="1">1</span> sachet de levure boulangère sèche (env. 6g)
- [ ] <span class="qty" data-base="3">3</span> cuillères à soupe de lait tiède
- [ ] <span class="qty" data-base="2">2</span> œufs entiers
- [ ] <span class="qty" data-base="70">70</span> g de beurre mou en dés
- [ ] <span class="qty" data-base="5">5</span> g de sel
- [ ] <span class="qty" data-base="350">350</span> g de fromage Maroilles
- [ ] <span class="qty" data-base="3">3</span> cuillères à soupe de crème fraîche épaisse
- [ ] <span class="qty" data-base="1">1</span> pincée de poivre du moulin

## 🥣 Instructions
1. **La pâte levée :** Délayez la levure dans le lait tiède. Dans un saladier (ou au robot), mélangez la farine et le sel. Ajoutez les œufs et le mélange lait-levure. Pétrissez 5 minutes.
2. **L'incorporation du beurre :** Ajoutez les dés de beurre mou et pétrissez encore 5 à 10 minutes jusqu'à obtenir une pâte souple et légèrement collante. Couvrez d'un torchon et laissez lever 1h15 dans un endroit chaud.
3. **Le fonçage :** Dégazez la pâte avec le poing. Étalez-la directement avec les mains dans un moule à tarte préalablement beurré et fariné. Laissez pousser à nouveau 20 minutes dans le moule.
4. **La garniture :** Préchauffez votre four à 200°C. Étalez la crème fraîche sur la pâte, poivrez légèrement. Grattez légèrement la croûte du Maroilles (ne la retirez pas, c'est là qu'est le goût !), coupez-le en tranches et disposez-les généreusement sur toute la tarte.
5. **La cuisson :** Enfournez pour 25 minutes. La pâte doit être bien gonflée, dorée, et le fromage doit bouillonner.

## 💡 Notes & Astuces
- **Accompagnement :** Servez cette flamiche bien chaude, accompagnée d'une salade verte bien assaisonnée pour contraster avec la richesse du fromage. 

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