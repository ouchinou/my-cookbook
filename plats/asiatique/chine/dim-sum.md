# 🥟 Dim Sum — Siu Mai (Raviolis Vapeur Ouverts)

> Le siu mai (燒賣) est le dim sum le plus emblématique des restaurants cantonais. Ces petits raviolis vapeur ouverts, farcis au porc et aux crevettes, se cuisinent en famille pour une expérience authentique.

| Préparation | Repos | Cuisson vapeur | Portions |
| :--- | :--- | :--- | :--- |
| 45 min | 15 min | 8 min | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. (~20 pièces) |

## 🛠 Matériel nécessaire
- [ ] Panier vapeur en bambou (ou cuiseur vapeur)
- [ ] Papier sulfurisé (pour tapisser le panier)

## 🛒 Ingrédients

### La pâte (ou utiliser des feuilles de wonton toutes prêtes)
- [ ] <span class="qty" data-base="200">200</span> g de farine T45
- [ ] <span class="qty" data-base="90">90</span> ml d'eau bouillante
- [ ] <span class="qty" data-base="1">1</span> pincée de sel

### La farce
- [ ] <span class="qty" data-base="250">250</span> g de porc haché (épaule, gras inclus)
- [ ] <span class="qty" data-base="150">150</span> g de crevettes décortiquées (hachées grossièrement)
- [ ] <span class="qty" data-base="4">4</span> champignons shiitake (réhydratés ou frais, hachés finement)
- [ ] <span class="qty" data-base="2">2</span> oignons verts émincés
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe de sauce soja
- [ ] <span class="qty" data-base="1">1</span> cuillère à café d'huile de sésame
- [ ] <span class="qty" data-base="1">1</span> cuillère à café de sucre
- [ ] <span class="qty" data-base="1">1</span> cm de gingembre frais râpé
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe de fécule de maïs
- [ ] Poivre blanc

### Finition & service
- [ ] <span class="qty" data-base="20">20</span> petits pois (ou carotte râpée) pour décorer
- [ ] Sauce soja et piment rouge

## 🥣 Instructions

### 1. La pâte maison
1. Verser l'eau bouillante sur la farine avec le sel. Mélanger à la fourchette, puis pétrir 5 min jusqu'à obtenir une pâte lisse.
2. Couvrir d'un torchon humide et laisser reposer **15 min**.
3. Étaler très finement (2 mm). Découper des cercles de ⌀ 9-10 cm. *(Ou utiliser des feuilles de wonton toutes prêtes.)*

### 2. La farce
1. Hacher les crevettes grossièrement au couteau (pas en purée).
2. Mélanger le porc, les crevettes, les shiitake, les oignons verts, le gingembre.
3. Assaisonner : sauce soja, huile de sésame, sucre, fécule, poivre blanc. Bien malaxer à la main pour lier la farce.
4. Laisser reposer **15 min** au frigo (la farce se raffermit).

### 3. Façonnage
1. Placer une cuillère à soupe de farce au centre d'un disque de pâte.
2. Former un cercle avec le pouce et l'index de la main gauche. Appuyer la farce au centre avec le pouce droit pour lui donner la forme de "gobelet ouvert".
3. La pâte forme des plis sur les côtés. Tasser la farce.
4. Déposer un petit pois ou un morceau de carotte sur le dessus.

### 4. Cuisson vapeur
1. Tapisser le panier vapeur de papier sulfurisé percé de trous (ou utiliser des feuilles de laitue).
2. Disposer les siu mai sans qu'ils se touchent. Cuire à la vapeur **8 min** à couvert.
3. Servir immédiatement avec de la sauce soja.

## 💡 Notes & Astuces
- **Feuilles toutes prêtes :** Les feuilles de wonton ou gow gee (gyoza) vendues en épicerie asiatique sont un excellent raccourci.
- **Congélation :** Se congèlent crus sur plateau, puis transférés en sac. Cuire directement vapeur 10-12 min sans décongeler.
- **Le gras du porc :** Ne pas utiliser de porc trop maigre — une farce trop sèche sera moins bonne. Un peu de lard haché peut aider.

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
