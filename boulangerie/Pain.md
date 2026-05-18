# Le Pain Cocotte Sans Pétrissage

> Une méthode révolutionnaire et magique : aucun robot requis, c'est le temps qui travaille pour vous. Le résultat offre une croûte digne d'un artisan boulanger.

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 10 min (Repos 12h) | 45 min | <input type="number" id="servings" value="1" min="1" style="width: 50px; font-weight: bold;"> miche(s) |

## 🛒 Ingrédients
- [ ] <span class="qty" data-base="400">400</span> g de farine T55 ou T65
- [ ] <span class="qty" data-base="300">300</span> ml d'eau tiède
- [ ] <span class="qty" data-base="4">4</span> g de levure boulangère sèche (1 cuillère à café)
- [ ] <span class="qty" data-base="8">8</span> g de sel

## 🥣 Instructions
1. **Le mélange :** Dans un grand saladier, mélangez brièvement la farine, le sel et la levure. Versez l'eau tiède et remuez grossièrement à la cuillère en bois juste pour amalgamer le tout. La pâte doit être collante et hétérogène.
2. **La longue pousse :** Couvrez hermétiquement le saladier avec du film étirable. Laissez reposer entre 12h et 15h à température ambiante (idéalement toute une nuit). La pâte va tripler de volume et se couvrir de bulles.
3. **Le préchauffage :** Le lendemain, placez une cocotte en fonte vide avec son couvercle dans votre four et préchauffez à 240°C.
4. **Le transfert :** Farinez généreusement votre plan de travail. Y déposer délicatement la pâte collante, repliez-la deux ou trois fois sur elle-même pour former une boule grossière et déposez-la sur une feuille de papier cuisson.
5. **La cuisson :** Sortez prudemment la cocotte brûlante du four, retirez le couvercle. Soulevez la pâte grâce au papier cuisson et déposez le tout dans la cocotte. Remettez le couvercle et enfournez pour 30 minutes. Retirez le couvercle et prolongez la cuisson de 12 à 15 minutes pour faire dorer la croûte.

## 💡 Notes & Astuces
- **Pourquoi la cocotte ?** Le couvercle de la cocotte retient l'humidité naturelle qui s'échappe de la pâte. C'est cette vapeur d'eau qui crée une croûte ultra-croustillante et fine.
- Laissez refroidir le pain sur une grille au moins 1 heure avant de le couper.

---
[⬅ Retour à l'index](../README.md)

<script>
  const servingInput = document.getElementById('servings');
  const baseServings = 1; // Base pour 1 miche de pain

  servingInput.addEventListener('input', () => {
    const ratio = servingInput.value / baseServings;
    document.querySelectorAll('.qty').forEach(span => {
      const baseValue = parseFloat(span.getAttribute('data-base'));
      let newValue = Math.round((baseValue * ratio) * 10) / 10;
      span.textContent = newValue;
    });
  });
</script>