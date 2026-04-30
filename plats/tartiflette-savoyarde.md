# 🧀 Tartiflette Savoyarde Traditionnelle

> Le grand classique réconfortant des Alpes. Idéal après une journée de ski (ou une longue journée de debug).

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 20 min | 30 min | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. |

## 🛒 Ingrédients
- [ ] <span class="qty" data-base="1">1</span> kg de pommes de terre (type Charlotte ou Amandine)
- [ ] <span class="qty" data-base="1">1</span> Reblochon fermier (environ <span class="qty" data-base="450">450</span> g)
- [ ] <span class="qty" data-base="200">200</span> g de lardons fumés
- [ ] <span class="qty" data-base="2">2</span> oignons jaunes
- [ ] <span class="qty" data-base="2">2</span> cuillères à soupe de crème fraîche épaisse
- [ ] <span class="qty" data-base="1">1</span> gousse d'ail (pour le plat)
- [ ] <span class="qty" data-base="10">10</span> cl de vin blanc sec (type Apremont ou Abymes)
- [ ] Poivre du moulin (sel inutile à cause des lardons et du fromage)

## 🥣 Instructions

1. **Cuisson des patates :** Éplucher les pommes de terre, les couper en gros dés. Les faire cuire à la vapeur ou à l'eau pendant 10-15 min (elles doivent rester fermes).
2. **La garniture :** Émincer les oignons. Dans une poêle, faire suer les oignons avec les lardons. Déglacer avec le vin blanc et laisser réduire de moitié.
3. **Préparation du plat :** Frotter un plat à gratin avec la gousse d'ail coupée en deux.
4. **Le montage :** 
    - Déposer une couche de pommes de terre.
    - Ajouter le mélange oignons/lardons.
    - Ajouter la crème fraîche et poivrer.
    - Terminer par le reste des pommes de terre.
5. **Le fromage :** Couper le Reblochon en deux dans l'épaisseur (ou en quatre) et le déposer croûte vers le haut sur les pommes de terre.
6. **Gratinage :** Enfourner à **200°C** pendant environ 20 à 30 minutes jusqu'à ce que le fromage soit bien doré et fondant.

## 💡 Notes & Astuces
* **Test de qualité :** Le Reblochon doit avoir la croûte bien orangée avec un léger duvet blanc, signe d'un affinage réussi.
* **Variante :** Si vous n'avez pas de vin blanc, vous pouvez le remplacer par un petit trait de bouillon de légumes.
* **Accompagnement :** Servir impérativement avec une salade verte croquante pour compenser le gras du plat.

---
[⬅ Retour à l'index](../README.md)

<script>
  const servingInput = document.getElementById('servings');
  const baseServings = 4;

  servingInput.addEventListener('input', () => {
    const ratio = servingInput.value / baseServings;
    document.querySelectorAll('.qty').forEach(span => {
      const baseValue = parseFloat(span.getAttribute('data-base'));
      // Calcul avec arrondi à 1 décimale
      let newValue = Math.round((baseValue * ratio) * 10) / 10;
      span.textContent = newValue;
    });
  });
</script>