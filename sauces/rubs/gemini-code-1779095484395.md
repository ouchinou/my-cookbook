# Rub Sec Citronné pour Poissons & Crustacés

> Les poissons n'aiment pas les rubs trop lourds ou trop sucrés. Ce mélange sec mise sur la fraîcheur des herbes et le peps du sumac (une épice au goût naturellement citronné) pour créer une croûte légère sur des pavés de saumon, de cabillaud ou des brochettes de crevettes.

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 5 min | À sec | <input type="number" id="servings" value="3" min="1" style="width: 50px; font-weight: bold;"> pers. |

## 🛒 Ingrédients
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe d'aneth séché
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe de sumac (épice citronnée) ou d'écorce de citron séchée
- [ ] <span class="qty" data-base="1">1</span> cuillère à café d'ail en poudre
- [ ] <span class="qty" data-base="1">1</span> cuillère à café de sel fin
- [ ] <span class="qty" data-base="0.5">0.5</span> cuillère à café de piment d'Espelette (pour la couleur et le peps)

## 🥣 Instructions
1. **Le mix :** Mélangez délicatement tous les ingrédients secs dans un bol.
2. **L'enrobage :** Séchez vos pavés de poisson avec un essuie-tout. Saupoudrez le rub sur le côté chair (pas sur la peau).
3. **La cuisson :** Déposez sur le grill ou au fumoir (Mode **SMOKE** ou **GRILL Med**).

## 💡 Notes & Astuces
- Contrairement aux marinades liquides au citron qui attaquent la chair du poisson si on les laisse trop longtemps, ce rub sec aromatique peut être appliqué 30 minutes avant la cuisson sans aucun risque d'abîmer la texture délicate du poisson.

---
[⬅ Retour à l'index](../README.md)

<script>
  const servingInput = document.getElementById('servings');
  const baseServings = 3;

  servingInput.addEventListener('input', () => {
    const ratio = servingInput.value / baseServings;
    document.querySelectorAll('.qty').forEach(span => {
      const baseValue = parseFloat(span.getAttribute('data-base'));
      let newValue = Math.round((baseValue * ratio) * 10) / 10;
      span.textContent = newValue;
    });
  });
</script>