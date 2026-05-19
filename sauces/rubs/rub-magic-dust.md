# Rub Sec "Magic Dust" (L'Universel du Barbecue)

> Inspiré des légendes du BBQ américain, ce rub sec est une valeur sûre. Le sucre qu'il contient va caraméliser sous l'effet de la chaleur, tandis que les épices vont former une croûte aromatique irrésistible. Parfait pour les ribs (travers), le porc effiloché (pulled pork) ou le poulet au fumoir.

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 5 min | À sec | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. |

## 🛒 Ingrédients
- [ ] <span class="qty" data-base="3">3</span> cuillères à soupe de cassonade (ou sucre brun)
- [ ] <span class="qty" data-base="2">2</span> cuillères à soupe de paprika doux ou fumé
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe de sel fin
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe d'ail en poudre
- [ ] <span class="qty" data-base="1">1</span> cuillère à café de poivre noir moulu
- [ ] <span class="qty" data-base="1">1</span> cuillère à café d'oignon en poudre

## 🥣 Instructions
1. **Le mélange :** Dans un bocal ou un bol, rassemblez toutes les épices, le sel et la cassonade. Mélangez très énergiquement pour casser les morceaux de sucre et obtenir une poudre homogène.
2. **La préparation de la viande :** Essuyez parfaitement votre viande (le porc ou le poulet) avec du papier essuie-tout pour qu'elle soit bien sèche.
3. **Le massage (Le "Rub") :** Saupoudrez généreusement le mélange sur toutes les faces de la viande. Massez fermement avec les mains pour faire adhérer les épices à la chair. 
4. **La cuisson :** Enfournez directement dans le Ninja Woodfire (idéal en mode **SMOKE** à 120°C ou **ROAST**).

## 💡 Notes & Astuces
- **L'astuce du liant :** Si les épices glissent et n'accrochent pas à la viande, badigeonnez d'abord votre pièce d'une couche ultra-fine de moutarde classique. Rassurez-vous, le goût de la moutarde disparaît complètement à la cuisson, mais elle sert de "colle" parfaite pour le rub !

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