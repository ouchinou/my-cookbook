# 🫒 Tapenade Noire Provençale

> La puissance de l'olive noire alliée aux câpres.

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 10 min | 0 min | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. |

## 🛒 Ingrédients
- [ ] <span class="qty" data-base="200">200</span> g d'olives noires dénoyautées
- [ ] <span class="qty" data-base="50">50</span> g de câpres
- [ ] <span class="qty" data-base="4">4</span> filets d'anchois à l'huile
- [ ] <span class="qty" data-base="1">1</span> gousse d'ail
- [ ] <span class="qty" data-base="5">5</span> cl d'huile d'olive

## 🥣 Instructions
1. Mixer grossièrement les olives, les câpres, les anchois et l'ail.
2. Ajouter l'huile d'olive progressivement pour lier l'ensemble (la texture ne doit pas être une purée lisse, on veut garder du relief).
3. Poivrer (le sel n'est généralement pas nécessaire à cause des anchois et des câpres).

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