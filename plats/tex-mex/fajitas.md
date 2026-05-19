# 🌮 Fajitas au Poulet

> Le grand classique tex-mex : du poulet mariné et grillé avec des poivrons colorés, servi dans une tortilla chaude avec les accompagnements de votre choix. Un repas convivial et personnalisable.

| Préparation | Marinade | Cuisson | Portions |
| :--- | :--- | :--- | :--- |
| 15 min | 30 min | 15 min | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. |

## 🛒 Ingrédients

### La marinade
- [ ] <span class="qty" data-base="600">600</span> g de blanc de poulet (ou bifteck de bœuf)
- [ ] <span class="qty" data-base="3">3</span> cuillères à soupe d'huile d'olive
- [ ] <span class="qty" data-base="1">1</span> cuillère à café de cumin en poudre
- [ ] <span class="qty" data-base="1">1</span> cuillère à café de paprika fumé
- [ ] <span class="qty" data-base="0.5">0.5</span> cuillère à café d'ail en poudre
- [ ] <span class="qty" data-base="0.5">0.5</span> cuillère à café d'origan séché
- [ ] Jus d'un demi-citron vert
- [ ] Sel, poivre

### Les légumes
- [ ] <span class="qty" data-base="2">2</span> poivrons (1 rouge + 1 jaune ou vert)
- [ ] <span class="qty" data-base="1">1</span> oignon rouge

### Pour servir
- [ ] <span class="qty" data-base="8">8</span> tortillas de blé (taille moyenne)
- [ ] <span class="qty" data-base="100">100</span> g de fromage râpé (cheddar ou mexicain)
- [ ] <span class="qty" data-base="1">1</span> pot de crème fraîche (ou yaourt grec)
- [ ] Guacamole (voir recette)
- [ ] Salsa ou tomates en dés avec coriandre
- [ ] Citron vert

## 🥣 Instructions

### 1. Marinade
1. Couper le poulet en lanières d'environ 1 cm d'épaisseur.
2. Mélanger l'huile, le cumin, le paprika, l'ail en poudre, l'origan et le jus de citron vert.
3. Enrober le poulet, saler, poivrer. Laisser mariner **au moins 30 min** (idéalement 2 h au frigo).

### 2. Légumes
1. Émincer les poivrons et l'oignon en lanières.

### 3. Cuisson
1. Chauffer une poêle ou plancha à feu très vif (avec un filet d'huile).
2. **Poulet :** Saisir les lanières de poulet **4-5 min** en remuant jusqu'à coloration. Réserver au chaud.
3. **Légumes :** Dans la même poêle, faire sauter les poivrons et l'oignon à feu vif **5-6 min** jusqu'à légère caramélisation. Saler.
4. Remettre le poulet dans la poêle avec les légumes, mélanger 1 min.

### 4. Service
1. Faire chauffer les tortillas 30 secondes de chaque côté dans une poêle sèche.
2. Disposer tout en centre de table : poulet/légumes, fromage, crème, guacamole.
3. Chacun garnit sa tortilla et roule.

## 💡 Notes & Astuces
- **Bœuf :** Utiliser un morceau tendre (bavette, rumsteck) coupé en lanières fines. Réduire la cuisson à 2-3 min.
- **Tortillas maison :** Mélanger 300 g farine, 1 c.c. sel, 3 c.s. huile, 150 ml eau chaude. Pétrir, reposer 15 min, former des boules, étaler, cuire 1 min/côté.
- **Au four :** Mettre les tortillas garnies à 180 °C pendant 5 min pour une version "burrito-style".

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
