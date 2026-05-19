# Pâte à Pizza (Style Napolitaine Express)

> Une pâte à pizza classique, croustillante à l'extérieur et moelleuse à l'intérieur, avec un taux d'hydratation idéal de 62% pour un étalage facile à la main.

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 20 min (Repos 2h) | 10 min | <input type="number" id="servings" value="2" min="1" style="width: 50px; font-weight: bold;"> pizzas |

## 🛒 Ingrédients
- [ ] <span class="qty" data-base="400">400</span> g de farine T45 ou Tipo 00
- [ ] <span class="qty" data-base="250">250</span> ml d'eau tiède
- [ ] <span class="qty" data-base="1">1</span> sachet de levure boulangère sèche (env. 6g)
- [ ] <span class="qty" data-base="10">10</span> g de sel
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe d'huile d'olive

## 🥣 Instructions
1. **L'activation :** Délayez la levure boulangère sèche dans l'eau tiède et laissez reposer 5 minutes pour l'activer.
2. **Le mélange :** Dans un grand saladier ou le bol d'un robot, mélangez la farine et le sel. Versez l'eau avec la levure ainsi que l'huile d'olive.
3. **Le pétrissage :** Pétrissez pendant 10 minutes jusqu'à ce que la pâte devienne lisse, élastique et se détache des parois.
4. **La première pousse :** Formez une belle boule, déposez-la dans un saladier légèrement huilé, couvrez d'un torchon humide et laissez doubler de volume pendant 2 heures dans un endroit chaud (ou près d'un radiateur).
5. **Le façonnage :** Divisez la pâte selon le nombre de portions. Étalez chaque pâton à la main sur un plan de travail fariné, en partant du centre vers l'extérieur pour chasser l'air vers les bords (ne jamais utiliser de rouleau à pâtisserie).

## 💡 Notes & Astuces
- **Le secret des bords gonflés :** En étalant la pizza à la main sans écraser les bords (la *cornicione*), l'air reste emprisonné et gonflera superbement à la cuisson.
- **Cuisson :** Préchauffez votre four au maximum (250°C ou plus). Si vous avez une pierre à pizza, c'est le moment de l'utiliser !

---
[⬅ Retour à l'index](../README.md)

<script>
  const servingInput = document.getElementById('servings');
  const baseServings = 2; // Base pour 2 pizzas

  servingInput.addEventListener('input', () => {
    const ratio = servingInput.value / baseServings;
    document.querySelectorAll('.qty').forEach(span => {
      const baseValue = parseFloat(span.getAttribute('data-base'));
      let newValue = Math.round((baseValue * ratio) * 10) / 10;
      span.textContent = newValue;
    });
  });
</script>
