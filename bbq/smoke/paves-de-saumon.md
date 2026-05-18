# Pavés de Saumon Fumés à Chaud (Hot Smoking)

> Contrairement au saumon fumé à froid du commerce, le fumage à chaud cuit délicatement le poisson à basse température tout en lui injectant des arômes boisés intenses. Le saumon reste incroyablement juteux et s'effondre à la fourchette.

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 10 min (Repos 30 min) | 35 min | <input type="number" id="servings" value="3" min="1" style="width: 50px; font-weight: bold;"> pers. |

## 🛒 Ingrédients
- [ ] <span class="qty" data-base="3">3</span> pavés de saumon frais (avec la peau)
- [ ] <span class="qty" data-base="2">2</span> cuillères à soupe de cassonade ou de sucre brun
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe de gros sel
- [ ] <span class="qty" data-base="1">1</span> cuillère à café de poivre blanc ou noir moulu
- [ ] <span class="qty" data-base="1">1</span> gobelet de pellets Ninja (Mélange doux / All-Purpose de préférence)

## 🥣 Instructions
1. **Le salage rapide :** Mélangez la cassonade, le gros sel et le poivre. Saupoudrez ce mélange sur la chair des pavés de saumon. Laissez reposer 30 minutes au frais. Le sel et le sucre vont raffermir la chair et fixer les arômes de fumée.
2. **Le rinçage :** Rincez rapidement les pavés sous l'eau froide pour enlever l'excès de sel, puis essuyez-les parfaitement avec du papier essuie-tout.
3. **Le chargement :** Remplissez la boîte de fumage avec les pellets.
4. **La configuration :** Sélectionnez le mode **SMOKE**, réglez la température sur **105°C** et le temps sur **40 minutes**. Appuyez sur *START* pour lancer le cycle.
5. **La cuisson :** Lorsque l'appareil a fini sa phase d'allumage des pellets (*ADD FOOD*), déposez les pavés de saumon sur la grille, **côté peau vers le bas**. Fermez le couvercle.
6. **Le contrôle :** Laissez fumer jusqu'à ce que le saumon atteigne une température interne de 55°C à cœur (suivi via la sonde de ton Woodfire Connect). La cuisson prend généralement entre 30 et 40 minutes selon l'épaisseur.

## 💡 Notes & Astuces
- **Le petit indicateur visuel :** Ne vous inquiétez pas si de petites gouttes blanches apparaissent à la surface du saumon ; il s'agit de l'albumine, une protéine naturelle qui coagule à la cuisson, signe que votre saumon est prêt !

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