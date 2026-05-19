# 🌾 Pâte à Galettes de Sarrasin

> La base de toutes les galettes bretonnes. Une pâte sans gluten, simple à réaliser, qui demande juste un peu de repos pour révéler tout son caractère.

| Préparation | Repos | Cuisson | Portions |
| :--- | :--- | :--- | :--- |
| 10 min | 2 h | 2 min / galette | <input type="number" id="servings" value="8" min="1" style="width: 50px; font-weight: bold;"> galettes |

## 🛒 Ingrédients
- [ ] <span class="qty" data-base="330">330</span> g de farine de blé noir (sarrasin)
- [ ] <span class="qty" data-base="75">75</span> cl d'eau froide
- [ ] <span class="qty" data-base="10">10</span> g de gros sel
- [ ] <span class="qty" data-base="1">1</span> œuf (facultatif, pour la tenue et la couleur)
- [ ] Beurre demi-sel (pour la cuisson)

## 🥣 Instructions

1. **La pâte :** Dans un saladier, mélanger la farine de sarrasin et le gros sel.
2. **L'hydratation :** Verser l'eau en deux ou trois fois, en mélangeant énergiquement au fouet pour éviter les grumeaux.
3. **Le secret :** Ajouter l'œuf et battre la pâte vigoureusement (cela permet d'aérer la pâte et de lui donner une meilleure texture).
4. **Le repos :** Couvrir et laisser reposer au réfrigérateur pendant **au moins 2 heures**.
5. **La cuisson :**
    - Faire chauffer une poêle ou une crêpière avec une noisette de beurre demi-sel.
    - Verser une louche de pâte et l'étaler finement.
    - Laisser cuire environ 2 minutes, puis retourner quand les bords commencent à se décoller.

## 💡 Notes & Astuces
* **L'eau :** Utilisez de l'eau bien froide pour une meilleure texture.
* **Conservation :** La pâte se conserve 48 h au réfrigérateur, bien couverte.
* **Consistance :** Si la pâte est trop épaisse après le repos, rajouter un petit filet d'eau.

> 🥞 **Déclinaisons :** voir les garnitures dans [`plats/bretagne/`](../plats/bretagne/)

---
[⬅ Retour à la boulangerie](./README.md)

<script>
  const servingInput = document.getElementById('servings');
  const baseServings = 8;

  servingInput.addEventListener('input', () => {
    const ratio = servingInput.value / baseServings;
    document.querySelectorAll('.qty').forEach(span => {
      const baseValue = parseFloat(span.getAttribute('data-base'));
      let newValue = Math.round((baseValue * ratio) * 10) / 10;
      span.textContent = newValue;
    });
  });
</script>
