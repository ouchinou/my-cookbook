# 🫓 Quesadillas au Poulet & Cheddar

> Les quesadillas sont la recette tex-mex la plus rapide : deux tortillas grillées collées par le fromage fondu, garnies de poulet et de légumes. Croustillantes à l'extérieur, fondantes à l'intérieur.

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 15 min | 15 min | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. (8 quesadillas) |

## 🛒 Ingrédients

### La garniture
- [ ] <span class="qty" data-base="300">300</span> g de blanc de poulet cuit (émincé ou effiloché)
- [ ] <span class="qty" data-base="200">200</span> g de fromage râpé (cheddar + mozzarella)
- [ ] <span class="qty" data-base="1">1</span> poivron rouge (émincé et sauté)
- [ ] <span class="qty" data-base="0.5">0.5</span> oignon rouge (émincé)
- [ ] <span class="qty" data-base="1">1</span> cuillère à café de cumin
- [ ] <span class="qty" data-base="1">1</span> cuillère à café de paprika
- [ ] Sel, poivre
- [ ] <span class="qty" data-base="8">8</span> tortillas de blé (taille standard ⌀ 20 cm)

### Accompagnements
- [ ] Crème fraîche ou yaourt grec
- [ ] Salsa (tomates, oignon, coriandre, citron vert)
- [ ] Guacamole (voir recette)
- [ ] Coriandre fraîche

## 🥣 Instructions

### 1. Préparer la garniture
1. Faire sauter le poivron et l'oignon dans un peu d'huile à feu vif 5 min. Assaisonner.
2. Si le poulet est cru : émincer, assaisonner avec le cumin et le paprika, saisir à feu vif 5-6 min.
3. Si le poulet est cuit (reste de rôti, fajitas...) : l'assaisonner de cumin et paprika, réchauffer 2 min.

### 2. Assemblage & cuisson
1. Chauffer une grande poêle (ou plancha) à feu moyen, légèrement huilée.
2. Poser une tortilla dans la poêle. Répartir sur la moitié : une couche de fromage, le poulet, les légumes, encore un peu de fromage.
3. Replier l'autre moitié de la tortilla sur la garniture.
4. Cuire **2-3 min** jusqu'à ce que la face du dessous soit dorée.
5. Retourner délicatement et cuire **2 min** côté opposé.
6. Réserver sur une planche, couper en 3 triangles.
7. Répéter pour les autres tortillas.

## 💡 Notes & Astuces
- **Mélange fromages :** Le cheddar apporte le goût, la mozzarella l'élasticité. Le mélange 50/50 est idéal.
- **Variante végétarienne :** Remplacer le poulet par des haricots noirs, du maïs, du poivron grillé et de l'avocat.
- **Rapidité :** Pour les faire en grande quantité, utiliser le four à 200 °C sur une plaque avec du papier cuisson — 10 min en retournant à mi-cuisson.

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
