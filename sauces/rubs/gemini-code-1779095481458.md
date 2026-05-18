# Rub Sec "SPG" (Sel, Poivre, Ail) pour Bœuf

> Le trio minimaliste mais redoutable utilisé par tous les pitmasters textans. Il respecte et sublime le goût puissant du bœuf sans le masquer. Idéal pour les côtes de bœuf, les entrecôtes ou les faux-filets au mode Grill.

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 2 min | À sec | <input type="number" id="servings" value="2" min="1" style="width: 50px; font-weight: bold;"> pers. |

## 🛒 Ingrédients
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe de gros sel (ou fleur de sel)
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe de poivre noir concassé (moulu grossièrement)
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe d'ail en poudre

## 🥣 Instructions
1. **L'assemblage :** Mélangez les trois ingrédients à parts égales dans un récipient.
2. **L'application :** Saupoudrez généreusement sur votre belle pièce de bœuf (ex: côte de bœuf) environ 15 à 30 minutes avant de la cuire.
3. **La cuisson :** Saisissez au Ninja Woodfire en mode **GRILL (HI)**.

## 💡 Notes & Astuces
- **La granulométrie :** Pour un SPG parfait, essayez d'utiliser un poivre moulu grossièrement (type "moulin") plutôt qu'une poudre extra-fine. Cela crée un relief incroyable sous la dent après la saisie au grill.

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