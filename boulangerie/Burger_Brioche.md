# Pains Burger Briochés (Buns)

> Des pains à burger dorés, incroyablement légers et moelleux, parfaits pour sublimer vos burgers faits maison.

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 25 min (Repos 2h30) | 15 min | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> buns |

## 🛒 Ingrédients
- [ ] <span class="qty" data-base="300">300</span> g de farine T45
- [ ] <span class="qty" data-base="120">120</span> ml de lait tiède
- [ ] <span class="qty" data-base="60">60</span> ml d'eau tiède
- [ ] <span class="qty" data-base="15">15</span> g de sucre
- [ ] <span class="qty" data-base="6">6</span> g de sel
- [ ] <span class="qty" data-base="1">1</span> sachet de levure boulangère sèche (env. 6g)
- [ ] <span class="qty" data-base="30">30</span> g de beurre mou en dés
- [ ] <span class="qty" data-base="1">1</span> œuf entier (pour la pâte)
- [ ] <span class="qty" data-base="1">1</span> jaune d'œuf (pour la dorure)
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe de graines de sésame

## 🥣 Instructions
1. **L'amorçage :** Mélangez le lait, l'eau, le sucre et la levure dans un verre. Laissez agir 5 minutes jusqu'à l'apparition d'une légère mousse.
2. **Le premier pétrissage :** Dans le bol du robot (ou un saladier), versez la farine et le sel. Ajoutez l'œuf entier et le mélange liquide à base de levure. Pétrissez pendant 5 minutes à vitesse lente.
3. **L'intégration du beurre :** Ajoutez les dés de beurre mou un à un tout en continuant de pétrir à vitesse moyenne pendant 10 minutes. La pâte doit devenir lisse, brillante et élastique.
4. **La première pousse :** Couvrez d'un torchon humide et laissez lever 1h30 dans un endroit tiède.
5. **Le façonnage & Seconde pousse :** Divisez la pâte selon le nombre de portions. Façonnez chaque morceau en une boule bien ronde en tendant la pâte vers le dessous. Déposez-les sur une plaque avec du papier cuisson et aplatissez-les légèrement avec la paume de la main. Laissez lever à nouveau pendant 1 heure.
6. **La cuisson :** Préchauffez le four à 200°C. Badigeonnez délicatement le dessus des buns avec le jaune d'œuf dilué dans un filet d'eau, puis saupoudrez de graines de sésame. Enfournez pour 12 à 15 minutes jusqu'à ce qu'ils soient bien dorés.

## 💡 Notes & Astuces
- **Astuce conservation :** Une fois complètement refroidis, vous pouvez congeler les buns individuels dans des sacs hermétiques. Il suffira de les passer 5 minutes au four ou au grille-pain avant le montage de vos burgers.

---
[⬅ Retour à l'index](../README.md)

<script>
  const servingInput = document.getElementById('servings');
  const baseServings = 4; // Base pour 4 buns

  servingInput.addEventListener('input', () => {
    const ratio = servingInput.value / baseServings;
    document.querySelectorAll('.qty').forEach(span => {
      const baseValue = parseFloat(span.getAttribute('data-base'));
      let newValue = Math.round((baseValue * ratio) * 10) / 10;
      span.textContent = newValue;
    });
  });
</script>