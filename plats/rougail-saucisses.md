# 🇷🇪 Rougail Saucisses (Tradition Réunionnaise)

> Une recette authentique transmise par les anciens (Gramounes). "La Réunion dan cœur".

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 20 min | 40 min | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. |

## 🛒 Ingrédients
- [ ] <span class="qty" data-base="4">4</span> à 6 saucisses (type Montbéliard ou saucisses fumées de la Réunion)
- [ ] <span class="qty" data-base="3">3</span> oignons jaunes
- [ ] <span class="qty" data-base="5">5</span> tomates bien mûres
- [ ] <span class="qty" data-base="20">20</span> g de gingembre frais
- [ ] <span class="qty" data-base="2">2</span> cuillères à soupe d'huile neutre
- [ ] Sel (avec modération selon le dessalage)
- [ ] Piment (optionnel, selon les goûts)

## 🥣 Instructions

1. **Dessalage :** Faire bouillir les saucisses entières dans une grande casserole d'eau pendant 10-15 minutes pour les dessaler.
2. **Découpe :** Égoutter les saucisses et les couper en morceaux d'environ 2 cm.
3. **Préparation aromatique :** Hacher les oignons en longueur (émincés) et couper les tomates en petits dés.
4. **Le Pilon :** Écraser le gingembre dans un pilon avec un peu de sel.
5. **Friture (Étape cruciale) :** Dans une sauteuse avec un peu d'huile, faire frire les morceaux de saucisses jusqu'à ce qu'ils soient bien dorés.
6. **Cuisson des oignons :** Ajouter les oignons hachés. Bien remuer jusqu'à ce qu'ils soient dorés, puis ajouter le mélange gingembre/sel.
7. **Mijotage :** Ajouter les tomates. Mélanger et laisser cuire à petit feu pendant **15 à 20 minutes**. La sauce doit devenir épaisse et les tomates bien fondues.

## 💡 Notes & Astuces
* **Le secret :** La réussite réside dans la friture initiale des saucisses et la réduction de la sauce.
* **Accompagnement :** Servir avec du riz blanc et des "grains" (pois du cap, lentilles, haricots rouges ou blancs).
* **Le petit plus :** Accompagner d'un "rougail tomates" pimenté à part pour relever le tout.

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