# Marinade BBQ Light "Smoky & Sweet"

> Une alternative légère aux sauces BBQ du commerce souvent très riches en huile et en sirop de glucose. Elle offre un goût sucré-salé idéal pour des émincés de porc, des ailes de poulet (Wings) ou du tofu.

| Préparation | Repos conseillé | Portions |
| :--- | :--- | :--- |
| 5 min | 2h à 4h | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. |

## 🛒 Ingrédients
- [ ] <span class="qty" data-base="4">4</span> cuillères à soupe de coulis de tomate (passata)
- [ ] <span class="qty" data-base="2">2</span> cuillères à soupe de vinaigre de cidre
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe de Worcestershire sauce
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe de sirop d'agave (ou miel)
- [ ] <span class="qty" data-base="1">1</span> cuillère à café de paprika fumé

## 🥣 Instructions
1. **La texture :** Dans un bol, mélangez le coulis de tomate avec le vinaigre de cidre (l'acide) et la sauce Worcestershire (la profondeur).
2. **La touche sucrée :** Ajoutez le sirop d'agave et le paprika fumé pour l'illusion d'une vraie sauce de grill américain.
3. **L'application :** Badigeonnez généreusement vos viandes (parfait sur des morceaux de porc ou des pilons de poulet).
4. **Le repos :** Laissez reposer 2 heures au frais avant cuisson.

## 💡 Notes & Astuces
- Puisque cette marinade contient du sucre naturel (sirop d'agave), surveillez la fin de cuisson sur le grill pour éviter que l'extérieur ne noircisse trop vite. C'est en revanche la marinade parfaite pour le mode **SMOKE (basse température)**.

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