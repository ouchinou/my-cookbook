# La Véritable Flamiche au Maroilles

> Originaire de la région du Nord, cette tarte salée utilise une pâte levée briochée, moelleuse à souhait, sur laquelle fond le Maroilles, ce fromage au caractère affirmé mais d'une douceur incroyable une fois cuit.

> 🔗 **Base :** préparer d'abord la pâte → [Pâte Levée Briochée](../../boulangerie/pate-levee-briochee.md)

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 10 min (hors pâte) | 25 min | <input type="number" id="servings" value="6" min="1" style="width: 50px; font-weight: bold;"> pers. |

## 🛒 Ingrédients
- [ ] 1 pâte levée briochée (voir base)
- [ ] <span class="qty" data-base="350">350</span> g de fromage Maroilles
- [ ] <span class="qty" data-base="3">3</span> cuillères à soupe de crème fraîche épaisse
- [ ] <span class="qty" data-base="1">1</span> pincée de poivre du moulin

## 🥣 Instructions
1. **La pâte :** Préparer la [pâte levée briochée](../../boulangerie/pate-levee-briochee.md) (1 h 30 de repos au total). La foncer dans un moule beurré et fariné.
2. **La garniture :** Préchauffez votre four à 200°C. Étalez la crème fraîche sur la pâte, poivrez légèrement. Grattez légèrement la croûte du Maroilles (ne la retirez pas, c'est là qu'est le goût !), coupez-le en tranches et disposez-les généreusement sur toute la tarte.
3. **La cuisson :** Enfournez pour 25 minutes. La pâte doit être bien gonflée, dorée, et le fromage doit bouillonner.

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