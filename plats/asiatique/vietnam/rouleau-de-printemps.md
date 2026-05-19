# 🌯 Rouleaux de Printemps Frais

> Les rouleaux de printemps vietnamiens (Gỏi cuốn) sont servis frais, non frits. Légers, colorés et sains, ils laissent transparaître la garniture à travers la galette translucide.

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 30 min | 5 min | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. (~12 rouleaux) |

## 🛒 Ingrédients

### La garniture
- [ ] <span class="qty" data-base="12">12</span> grandes galettes de riz (⌀ 22 cm)
- [ ] <span class="qty" data-base="200">200</span> g de crevettes cuites décortiquées
- [ ] <span class="qty" data-base="80">80</span> g de vermicelles de riz
- [ ] <span class="qty" data-base="1">1</span> carotte (coupée en julienne)
- [ ] <span class="qty" data-base="0.5">0.5</span> concombre (coupé en julienne)
- [ ] <span class="qty" data-base="100">100</span> g de pousses de soja
- [ ] <span class="qty" data-base="6">6</span> feuilles de laitue (coupées en deux)
- [ ] <span class="qty" data-base="1">1</span> bouquet de menthe fraîche
- [ ] <span class="qty" data-base="0.5">0.5</span> bouquet de coriandre fraîche

### Sauce cacahuète (ou nuoc-cham)
- [ ] <span class="qty" data-base="3">3</span> cuillères à soupe de beurre de cacahuète
- [ ] <span class="qty" data-base="2">2</span> cuillères à soupe de sauce hoisin
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe de sauce soja
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe de jus de citron vert
- [ ] <span class="qty" data-base="2">2</span> cuillères à soupe d'eau chaude
- [ ] Piment (optionnel)

## 🥣 Instructions

### 1. Préparer les garnitures
1. **Vermicelles :** Cuire les vermicelles selon les instructions (trempage eau chaude 5-10 min). Rincer, égoutter et réserver.
2. **Légumes :** Couper la carotte et le concombre en julienne fine.
3. **Crevettes :** Couper chaque crevette en deux dans l'épaisseur (pour la belle présentation à travers la galette).

### 2. Sauce
1. Mélanger le beurre de cacahuète, la sauce hoisin, la sauce soja et le jus de citron vert.
2. Détendre avec l'eau chaude jusqu'à consistance de sauce nappante. Goûter, ajuster.

### 3. Roulage
1. **Ramollir la galette :** Tremper une galette 10-15 secondes dans de l'eau tiède jusqu'à ce qu'elle soit souple mais pas trop collante. Poser sur un plan propre.
2. **Garnir :** Au centre-bas de la galette, déposer : une demi-feuille de laitue, puis les vermicelles, carotte, concombre, pousses de soja, menthe, coriandre.
3. **Crevettes en vitrine :** Poser 2-3 demi-crevettes (côté rose vers vous) sur la partie basse de la galette — elles seront visibles à travers.
4. **Rouler :** Rabattre le bas sur la garniture, rouler d'un quart, rabattre les côtés, puis finir de rouler.
5. Poser côté fermé vers le bas. Servir rapidement (ne pas préparer plus de 30 min à l'avance).

## 💡 Notes & Astuces
- **La galette :** Elle ne doit pas tremper trop longtemps — elle continue de ramollir après la sortie de l'eau.
- **Variante :** Remplacer les crevettes par du tofu grillé ou du poulet cuit.
- **Conservation :** Couvrir d'un torchon humide si les rouleaux attendent avant le service.

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
