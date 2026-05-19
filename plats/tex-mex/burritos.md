# 🌯 Burritos au Bœuf & Haricots Rouges

> Le burrito est l'emblème de la street food tex-mex : une grande tortilla bien garnie, roulée serrée. La clé est d'avoir une farce généreuse mais bien sèche pour éviter que ça détrempe.

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 20 min | 25 min | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. (4 burritos) |

## 🛒 Ingrédients

### La garniture viande
- [ ] <span class="qty" data-base="400">400</span> g de bœuf haché (ou poulet émincé)
- [ ] <span class="qty" data-base="1">1</span> oignon émincé
- [ ] <span class="qty" data-base="2">2</span> gousses d'ail hachées
- [ ] <span class="qty" data-base="400">400</span> g de haricots rouges en conserve (égouttés)
- [ ] <span class="qty" data-base="200">200</span> g de maïs en conserve (égoutté)
- [ ] <span class="qty" data-base="1">1</span> cuillère à café de cumin
- [ ] <span class="qty" data-base="1">1</span> cuillère à café de paprika fumé
- [ ] <span class="qty" data-base="0.5">0.5</span> cuillère à café de chili en poudre
- [ ] <span class="qty" data-base="2">2</span> cuillères à soupe de concentré de tomates
- [ ] <span class="qty" data-base="5">5</span> cl d'eau
- [ ] <span class="qty" data-base="2">2</span> cuillères à soupe d'huile d'olive
- [ ] Sel, poivre

### Le riz
- [ ] <span class="qty" data-base="200">200</span> g de riz long
- [ ] <span class="qty" data-base="1">1</span> cube de bouillon de poulet
- [ ] Jus d'un demi-citron vert
- [ ] Coriandre fraîche

### Pour assembler
- [ ] <span class="qty" data-base="4">4</span> grandes tortillas de blé (⌀ 25-30 cm)
- [ ] <span class="qty" data-base="120">120</span> g de fromage râpé (cheddar)
- [ ] <span class="qty" data-base="1">1</span> pot de crème fraîche (ou yaourt grec)
- [ ] <span class="qty" data-base="1">1</span> avocat (tranché ou guacamole)

## 🥣 Instructions

### 1. Le riz
1. Cuire le riz dans de l'eau bouillante salée avec le cube de bouillon selon les instructions.
2. Une fois cuit, assaisonner avec le jus de citron vert et de la coriandre hachée. Réserver.

### 2. La garniture viande
1. Faire revenir l'oignon et l'ail dans l'huile à feu moyen (3 min).
2. Ajouter la viande hachée, monter le feu, colorer en écrasant les grumeaux.
3. Incorporer le cumin, le paprika, le chili. Mélanger 1 min.
4. Ajouter le concentré de tomates et l'eau. Mélanger, laisser réduire 5 min à feu doux.
5. Incorporer les haricots rouges et le maïs. Cuire encore 3 min. Ajuster l'assaisonnement. La farce doit être humide mais pas liquide.

### 3. Assemblage
1. Réchauffer les tortillas 30 secondes au micro-ondes (ou dans une poêle sèche).
2. Au centre de chaque tortilla : déposer une couche de riz, puis la garniture viande, le fromage, une cuillère de crème, l'avocat.
3. **Rouler serré :** Rabattre le bas sur la garniture, puis les deux côtés, et rouler du bas vers le haut.
4. Faire griller le burrito plié dans une poêle chaude 1-2 min de chaque côté pour le sceller et le réchauffer.

## 💡 Notes & Astuces
- **La tortilla :** Elle doit être bien chaude et souple pour ne pas se déchirer au roulage.
- **Version poulet :** Utiliser du poulet cuit effiloché avec une marinade tex-mex (voir recette fajitas).
- **Gratinés :** Mettre les burritos au four à 200 °C avec du fromage sur le dessus pendant 8 min.

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
