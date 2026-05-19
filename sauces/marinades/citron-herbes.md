# Marinade Légère Citron & Herbes Fraîches

> Une marinade méditerranéenne ultra-fraîche, idéale pour les blancs de volaille, les pavés de poisson blanc ou les brochettes de légumes. L'acidité du citron attendrit la viande sans aucun apport calorique superflu.

| Préparation | Repos conseillé | Portions |
| :--- | :--- | :--- |
| 5 min | 30 min à 2h | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. |

## 🛒 Ingrédients
- [ ] <span class="qty" data-base="2">2</span> citrons jaunes (jus et zestes)
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe d'huile d'olive
- [ ] <span class="qty" data-base="2">2</span> gousses d'ail émincées
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe d'herbes de Provence (ou origan)
- [ ] <span class="qty" data-base="1">1</span> pincée de sel et poivre noir

## 🥣 Instructions
1. **Le zeste :** Prélevez le zeste d'un citron, puis pressez le jus des deux citrons dans un récipient.
2. **L'émulsion légère :** Ajoutez l'unique cuillère d'huile d'olive, l'ail émincé et les herbes. Fouettez énergiquement.
3. **Le bain :** Plongez vos aliments (poulet, poisson ou légumes) dans la marinade. Assurez-vous que tout soit bien enrobé.
4. **Le repos :** Couvrez et laissez reposer au frais (30 min pour le poisson, 1 à 2h pour le poulet) avant de passer au Ninja Woodfire (Mode Grill ou Air Fry).

## 💡 Notes & Astuces
- **Alerte texture :** Ne laissez pas le poisson mariner plus de 30 minutes dans cette préparation, car l'acide du citron risquerait de "cuire" la chair et de la rendre friable.

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