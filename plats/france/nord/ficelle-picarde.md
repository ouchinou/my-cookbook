# 🥞 Ficelle Picarde

> Spécialité de Picardie (Hauts-de-France), la ficelle picarde est une crêpe garnie de jambon, de champignons à la crème, roulée et gratinée sous le fromage. Un plat généreux qui réunit le meilleur du Nord.

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 25 min | 30 min | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. (4 ficelles) |

## 🛒 Ingrédients

### Les crêpes
- [ ] <span class="qty" data-base="150">150</span> g de farine
- [ ] <span class="qty" data-base="2">2</span> œufs
- [ ] <span class="qty" data-base="300">300</span> ml de lait
- [ ] <span class="qty" data-base="1">1</span> pincée de sel
- [ ] <span class="qty" data-base="15">15</span> g de beurre fondu

### La garniture champignons-crème
- [ ] <span class="qty" data-base="300">300</span> g de champignons de Paris (émincés)
- [ ] <span class="qty" data-base="1">1</span> échalote finement émincée
- [ ] <span class="qty" data-base="15">15</span> cl de crème fraîche épaisse
- [ ] <span class="qty" data-base="20">20</span> g de beurre
- [ ] Sel, poivre, noix de muscade

### La béchamel légère
- [ ] <span class="qty" data-base="25">25</span> g de beurre
- [ ] <span class="qty" data-base="25">25</span> g de farine
- [ ] <span class="qty" data-base="250">250</span> ml de lait
- [ ] Sel, poivre, noix de muscade

### Assemblage
- [ ] <span class="qty" data-base="4">4</span> tranches de jambon blanc (jambon supérieur)
- [ ] <span class="qty" data-base="100">100</span> g de gruyère râpé (ou emmental)

## 🥣 Instructions

### 1. Les crêpes
1. Mélanger farine, sel, œufs battus, puis incorporer le lait progressivement pour éviter les grumeaux.
2. Ajouter le beurre fondu. Laisser reposer 15 min.
3. Cuire **4 grandes crêpes** dans une crêpière beurrée. Réserver.

### 2. La garniture champignons
1. Faire suer l'échalote dans le beurre 2 min.
2. Ajouter les champignons émincés, cuire à feu vif jusqu'à évaporation de l'eau (5-7 min).
3. Verser la crème fraîche, assaisonner sel, poivre, muscade. Laisser épaissir 2-3 min.

### 3. La béchamel
1. Faire fondre le beurre dans une casserole. Incorporer la farine d'un coup, remuer 1 min.
2. Verser le lait progressivement en fouettant pour éviter les grumeaux.
3. Cuire à feu moyen en remuant jusqu'à épaississement (5 min). Assaisonner.

### 4. Assemblage & gratinage
1. Préchauffer le four à **200 °C** (gril si possible).
2. Sur chaque crêpe : déposer une tranche de jambon, puis 2-3 cuillères de garniture champignons.
3. Rouler chaque crêpe en boudin.
4. Disposer les ficelles dans un plat à gratin beurré.
5. Napper de béchamel sur l'ensemble. Parsemer de gruyère râpé.
6. Gratiner au four **10-15 min** jusqu'à coloration dorée.

## 💡 Notes & Astuces
- **Préparation à l'avance :** Les ficelles peuvent être montées (sans béchamel) la veille. Napper et gratiner au moment.
- **Champignons :** Bien les faire sauter jusqu'à évaporation complète — sinon la garniture sera trop liquide et va détremper la crêpe.
- **Variante :** Ajouter quelques crevettes roses dans la garniture pour une ficelle picarde "mer".

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
