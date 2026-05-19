# � La Galette Complète

> La déclinaison la plus emblématique de la Bretagne : le trio œuf-jambon-fromage sur une galette de sarrasin bien croustillante. Simple, généreux, indémodable.

> 🔗 **Base :** préparer d'abord la pâte → [Pâte à Galettes de Sarrasin](../../../boulangerie_pates/galette-sarrasin.md)

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 5 min | 4 min | <input type="number" id="servings" value="1" min="1" style="width: 50px; font-weight: bold;"> galette(s) |

## 🛒 Ingrédients (par galette)
- [ ] <span class="qty" data-base="1">1</span> galette de sarrasin cuite (voir base)
- [ ] <span class="qty" data-base="1">1</span> œuf
- [ ] <span class="qty" data-base="1">1</span> tranche de jambon blanc
- [ ] <span class="qty" data-base="30">30</span> g d'emmental râpé (ou comté)
- [ ] Beurre demi-sel
- [ ] Sel, poivre

## 🥣 Instructions

1. **Chauffer** la crêpière avec une noisette de beurre demi-sel.
2. **Déposer** une galette sur la crêpière chaude.
3. **Garnir :** Répartir l'emmental râpé sur la galette, casser l'œuf au centre, poser le jambon.
4. **Plier :** Rabattre les quatre bords vers le centre pour former un carré.
5. **Finir** la cuisson 1-2 minutes jusqu'à ce que l'œuf soit cuit à votre goût.
6. **Assaisonner** légèrement et servir immédiatement.

## 💡 Notes & Astuces
* **Variantes :** Remplacer le jambon par du saumon fumé, des champignons sautés, de l'andouille de Guémené...
* **Le fromage :** Le comté ou le gruyère apportent plus de caractère que l'emmental.
* **L'œuf :** Pour un jaune coulant, couvrir la crêpière 1 minute en fin de cuisson.

---
[⬅ Retour à l'index](../README.md)

<script>
  const servingInput = document.getElementById('servings');
  const baseServings = 1;

  servingInput.addEventListener('input', () => {
    const ratio = servingInput.value / baseServings;
    document.querySelectorAll('.qty').forEach(span => {
      const baseValue = parseFloat(span.getAttribute('data-base'));
      let newValue = Math.round((baseValue * ratio) * 10) / 10;
      span.textContent = newValue;
    });
  });
</script>