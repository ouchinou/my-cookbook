# 🥩 Boles de Picolat (Boulettes au Piment d'Espelette)

> Spécialité catalane de Perpignan, les "boles de picolat" sont des boulettes de viande mijotées dans une sauce tomate parfumée aux olives vertes et aux câpres. Un plat dominical emblématique des Pyrénées.

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 30 min | 1 h | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. (~20 boulettes) |

## 🛒 Ingrédients

### Les boulettes
- [ ] <span class="qty" data-base="400">400</span> g de bœuf haché
- [ ] <span class="qty" data-base="200">200</span> g de porc haché
- [ ] <span class="qty" data-base="2">2</span> gousses d'ail hachées
- [ ] <span class="qty" data-base="2">2</span> cuillères à soupe de persil plat haché
- [ ] <span class="qty" data-base="1">1</span> œuf
- [ ] <span class="qty" data-base="50">50</span> g de mie de pain trempée dans le lait
- [ ] <span class="qty" data-base="1">1</span> cuillère à café de piment d'Espelette
- [ ] Sel, poivre
- [ ] Farine (pour paner légèrement)
- [ ] Huile d'olive (pour dorer)

### La sauce
- [ ] <span class="qty" data-base="3">3</span> tomates bien mûres (ou 400 g de tomates pelées en conserve)
- [ ] <span class="qty" data-base="1">1</span> oignon émincé
- [ ] <span class="qty" data-base="2">2</span> gousses d'ail
- [ ] <span class="qty" data-base="1">1</span> poivron vert (coupé en dés)
- [ ] <span class="qty" data-base="80">80</span> g d'olives vertes dénoyautées
- [ ] <span class="qty" data-base="20">20</span> g de câpres
- [ ] <span class="qty" data-base="15">15</span> cl de vin blanc sec
- [ ] <span class="qty" data-base="3">3</span> cuillères à soupe d'huile d'olive
- [ ] <span class="qty" data-base="1">1</span> cuillère à café de piment d'Espelette
- [ ] Sel, poivre

## 🥣 Instructions

### 1. Les boulettes
1. **La panade :** Émietter la mie de pain, la tremper dans un peu de lait, l'essorer.
2. **Mélange :** Combiner les deux viandes, l'ail, le persil, l'œuf, la panade et le piment d'Espelette. Saler, poivrer.
3. **Former :** Rouler en boulettes de la taille d'une noix (~30 g). Rouler légèrement dans la farine.
4. **Dorer :** Faire chauffer l'huile dans une cocotte. Dorer les boulettes sur toutes les faces à feu vif (3 min). Réserver.

### 2. La sauce
1. Dans la même cocotte, faire revenir l'oignon et l'ail à feu moyen 3-4 min.
2. Ajouter le poivron vert, cuire 3 min.
3. Incorporer les tomates (mondées et concassées si fraîches). Laisser cuire 5 min.
4. Déglacer au vin blanc, réduire de moitié.
5. Assaisonner avec le piment d'Espelette, sel et poivre.

### 3. Mijotage
1. Remettre les boulettes dans la sauce. Couvrir.
2. Mijoter à feu doux **40 min** en remuant délicatement de temps en temps.
3. Ajouter les olives vertes et les câpres les **10 dernières minutes**.
4. Goûter et rectifier l'assaisonnement.

## 💡 Notes & Astuces
- **Le piment d'Espelette :** Fruité et peu piquant, il est irremplaçable dans cette recette. On peut le trouver en épicerie fine ou commander en ligne.
- **Accompagnement traditionnel :** Servir avec des haricots blancs à la catalane, du riz ou des pâtes fraîches.
- **Le lendemain :** Comme tous les plats mijotés, les boles de picolat sont encore meilleures réchauffées.

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
