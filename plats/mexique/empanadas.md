# 🥟 Empanadas (Chaussons Farcis)

> Originaires d'Argentine et d'Espagne, ces chaussons farcis au bœuf épicé sont cuits au four pour une version plus légère. La pâte maison est feuilletée et dorée, la farce généreuse et parfumée.

| Préparation | Repos | Cuisson | Portions |
| :--- | :--- | :--- | :--- |
| 40 min | 30 min | 20 min | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. (~12 empanadas) |

## 🛒 Ingrédients

### La pâte
- [ ] <span class="qty" data-base="300">300</span> g de farine T55
- [ ] <span class="qty" data-base="80">80</span> g de beurre froid coupé en dés
- [ ] <span class="qty" data-base="1">1</span> œuf entier
- [ ] <span class="qty" data-base="7">7</span> cl d'eau froide
- [ ] <span class="qty" data-base="5">5</span> g de sel
- [ ] 1 jaune d'œuf (dorure)

### La farce
- [ ] <span class="qty" data-base="300">300</span> g de bœuf haché (ou mélange bœuf/porc)
- [ ] <span class="qty" data-base="1">1</span> oignon finement émincé
- [ ] <span class="qty" data-base="2">2</span> gousses d'ail hachées
- [ ] <span class="qty" data-base="1">1</span> poivron rouge (brunoise)
- [ ] <span class="qty" data-base="2">2</span> tomates (épépinées et coupées en dés)
- [ ] <span class="qty" data-base="1">1</span> cuillère à café de cumin en poudre
- [ ] <span class="qty" data-base="1">1</span> cuillère à café de paprika fumé
- [ ] <span class="qty" data-base="0.5">0.5</span> cuillère à café d'origan séché
- [ ] <span class="qty" data-base="2">2</span> cuillères à soupe d'huile d'olive
- [ ] Sel, poivre
- [ ] <span class="qty" data-base="2">2</span> œufs durs (hachés — apportent de la tenue à la farce)

## 🥣 Instructions

### 1. La pâte
1. **Sabler :** Dans un saladier, mélanger la farine et le sel. Incorporer le beurre froid du bout des doigts jusqu'à obtenir un mélange sableux.
2. **Lier :** Ajouter l'œuf battu et l'eau froide progressivement. Pétrir rapidement juste pour former une boule homogène.
3. **Repos :** Envelopper dans du film alimentaire et réfrigérer **30 min**.

### 2. La farce
1. Faire revenir l'oignon et l'ail dans l'huile d'olive à feu moyen jusqu'à transparence.
2. Ajouter le poivron, cuire 3 min. Incorporer la viande hachée, monter le feu et colorer.
3. Ajouter les tomates, le cumin, le paprika et l'origan. Mélanger, saler et poivrer.
4. Laisser mijoter **10 min** jusqu'à ce que la farce soit sèche. Laisser refroidir complètement.
5. Incorporer les œufs durs hachés.

### 3. Montage & cuisson
1. Préchauffer le four à **200 °C**.
2. Étaler la pâte à 3 mm d'épaisseur. Découper des cercles de ⌀ 12 cm (un bol retourné fait l'affaire).
3. Déposer 1 cuillère à soupe de farce au centre. Humecter le bord avec un peu d'eau.
4. Plier en demi-lune et souder les bords en appuyant fort. Faire des croisillons avec une fourchette.
5. Dorer au jaune d'œuf dilué. Enfourner **18-20 min** jusqu'à belle dorure.

## 💡 Notes & Astuces
- **Version frite :** Frire dans de l'huile à 180 °C, 4 min de chaque côté pour une version plus croustillante.
- **Variante poulet :** Remplacer le bœuf par du poulet effiloché avec poivrons et olive.
- **Congélation :** Se congèlent crus. Cuire directement au four en ajoutant 5 min.

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
