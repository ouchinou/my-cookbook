# 🥟 Bánh Bao (Petits Pains Farcis à la Vapeur)

> Les bánh bao (banh bao) sont des petits pains moelleux cuits à la vapeur, fourrés d'une farce savoureuse. Emblématiques de la cuisine de rue vietnamienne, leur pâte doit être aérienne et brillante.

| Préparation | Repos | Cuisson vapeur | Portions |
| :--- | :--- | :--- | :--- |
| 40 min | 1 h 30 | 15 min | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. (8 bao) |

## 🛠 Matériel nécessaire
- [ ] Panier vapeur en bambou (ou cuiseur vapeur)
- [ ] Carrés de papier sulfurisé (5 x 5 cm par bao)

## 🛒 Ingrédients

### La pâte
- [ ] <span class="qty" data-base="300">300</span> g de farine T45 (ou farine de blé à gâteau de riz)
- [ ] <span class="qty" data-base="150">150</span> ml de lait chaud (ou eau)
- [ ] <span class="qty" data-base="7">7</span> g de levure boulangère sèche
- [ ] <span class="qty" data-base="20">20</span> g de sucre
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe d'huile neutre
- [ ] <span class="qty" data-base="0.5">0.5</span> cuillère à café de sel
- [ ] <span class="qty" data-base="0.5">0.5</span> cuillère à café de levure chimique (pour plus de légèreté)

### La farce
- [ ] <span class="qty" data-base="200">200</span> g de porc haché (ou poulet)
- [ ] <span class="qty" data-base="2">2</span> œufs durs (coupés en quartiers)
- [ ] <span class="qty" data-base="2">2</span> oignons verts émincés
- [ ] <span class="qty" data-base="2">2</span> champignons noirs séchés (réhydratés et hachés)
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe de sauce hoisin
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe de sauce soja
- [ ] <span class="qty" data-base="0.5">0.5</span> cuillère à café de cinq-épices
- [ ] <span class="qty" data-base="1">1</span> cuillère à café d'huile de sésame
- [ ] Poivre, sel

## 🥣 Instructions

### 1. La pâte
1. **Activer la levure :** Mélanger la levure avec le lait chaud et le sucre. Laisser mousser 10 min.
2. **Pétrir :** Mélanger farine, sel, levure chimique. Creuser un puits, ajouter le mélange levure + l'huile. Pétrir 10 min jusqu'à pâte lisse et souple.
3. **Première pousse :** Couvrir et laisser lever **1 h** dans un endroit chaud (la pâte doit doubler).

### 2. La farce
1. Faire revenir l'oignon vert dans un peu d'huile 2 min.
2. Ajouter le porc haché, colorer en émiettant.
3. Assaisonner avec la sauce hoisin, la sauce soja, le cinq-épices et l'huile de sésame.
4. Incorporer les champignons. Saler, poivrer. Laisser refroidir complètement.

### 3. Façonnage
1. **Dégazer** la pâte. Diviser en 8 boules égales (~60 g).
2. Aplatir chaque boule en disque de ⌀ 12 cm (bords plus fins que le centre).
3. Déposer au centre : 1 cuillère de farce + 1 quartier d'œuf dur.
4. Rassembler les bords vers le haut en plissant pour fermer. Placer sur un carré de papier sulfurisé, plissures vers le bas.
5. Couvrir et laisser gonfler **30 min**.

### 4. Cuisson vapeur
1. Porter l'eau à ébullition dans le cuiseur vapeur.
2. Disposer les bao (avec leur carré de papier) dans le panier sans qu'ils se touchent.
3. Cuire à vapeur intense **15 min** sans soulever le couvercle.
4. Éteindre le feu et laisser reposer **2 min** avant d'ouvrir (évite que la pâte se ratatine).

## 💡 Notes & Astuces
- **La couleur blanche :** La pâte à bánh bao doit rester blanche — ne pas dorer. C'est la vapeur qui cuit tout.
- **Congélation :** Les bao cuits se congèlent très bien. Réchauffer à la vapeur 5-6 min (pas au micro-ondes, la pâte durcirait).
- **Variante sucrée :** Remplacer la farce salée par de la pâte de lotus ou de la crème de cacahuète pour des bánh bao dessert.

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
