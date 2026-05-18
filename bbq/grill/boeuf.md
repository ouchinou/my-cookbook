# Belles Pièces de Bœuf Grillées & Sa Marinade Maître Grill

> Le secret d'une viande de bœuf d'exception au Ninja Woodfire : une saisie à très haute température pour marquer la viande, précédée ou non d'une marinade qui attendrit les fibres. Idéal pour une côte de bœuf, une entrecôte ou un faux-filet.

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 10 min (Option marinade 1h) | 12 min | <input type="number" id="servings" value="2" min="1" style="width: 50px; font-weight: bold;"> pers. |

## 🛒 Ingrédients
- [ ] <span class="qty" data-base="2">2</span> belles pièces de bœuf (ex: faux-filet de 300g)
- [ ] <span class="qty" data-base="3">3</span> cuillères à soupe d'huile d'olive
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe de sauce soja
- [ ] <span class="qty" data-base="1">1</span> gousse d'ail écrasée
- [ ] <span class="qty" data-base="1">1</span> branche de romarin frais
- [ ] <span class="qty" data-base="1">1</span> cuillère à café de fleur de sel et poivre noir

## 🥣 Instructions
1. **La marinade (Optionnelle) :** Dans un plat, mélangez l'huile d'olive, la sauce soja, l'ail et le romarin. Déposez la viande et retournez-la pour bien l'enrober. Laissez mariner à température ambiante 1 heure avant la cuisson. Si vous préférez la viande nature, masquez-la simplement d'un filet d'huile, de sel et de poivre juste avant de griller.
2. **La configuration :** Sélectionnez le mode **GRILL**, réglez la température sur **HI (Élevée)**. Réglez le temps sur 10 à 15 minutes selon l'épaisseur. Appuyez sur *START* pour lancer le préchauffage.
3. **La saisie :** Lorsque l'appareil affiche *ADD FOOD*, déposez la viande sur la grille bien chaude. Fermez le couvercle.
4. **Le retournement :** Laissez cuire sans ouvrir pendant la moitié du temps (ex: 4 minutes pour un faux-filet saignant), ouvrez, retournez la viande, puis fermez pour terminer la cuisson. *(Pour une côte de bœuf épaisse, utilisez la sonde Connect intégrée et visez 52°C à cœur pour une cuisson saignante).*
5. **Le repos :** Retirez la viande et laissez-la reposer sur une planche sous une feuille d'aluminium pendant 5 minutes avant de la découper.

## 💡 Notes & Astuces
- **Pourquoi le repos ?** Le repos permet aux jus de se redistribuer au cœur des chairs. Si vous coupez la viande immédiatement, tout le jus s'échappera et la viande sera sèche.

---
[⬅ Retour à l'index](../README.md)

<script>
  const servingInput = document.getElementById('servings');
  const baseServings = 2;

  servingInput.addEventListener('input', () => {
    const ratio = servingInput.value / baseServings;
    document.querySelectorAll('.qty').forEach(span => {
      const baseValue = parseFloat(span.getAttribute('data-base'));
      let newValue = Math.round((baseValue * ratio) * 10) / 10;
      span.textContent = newValue;
    });
  });
</script>