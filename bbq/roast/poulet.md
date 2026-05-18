# Poulet Crapaudine Rôti et Parfumé au Feu de Bois

> La fonction Rôtissage (Roast) combinée à la technologie Woodfire donne un poulet à la peau ultra-croustillante avec le goût inimitable d'un poulet cuit au feu de bois. La découpe en crapaudine (à plat) assure une cuisson parfaitement uniforme.

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 15 min | 45 min | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. |

## 🛒 Ingrédients
- [ ] <span class="qty" data-base="1">1</span> poulet entier d'environ 1,2 kg
- [ ] <span class="qty" data-base="2">2</span> cuillères à soupe d'huile d'olive
- [ ] <span class="qty" data-base="1">1</span> cuillère à soupe de paprika doux
- [ ] <span class="qty" data-base="1">1</span> cuillère à café d'ail en poudre
- [ ] <span class="qty" data-base="1">1</span> cuillère à café de sel fin
- [ ] <span class="qty" data-base="1">1</span> gobelet de pellets Ninja (Mélange doux ou polyvalent)

## 🥣 Instructions
1. **La découpe en crapaudine :** À l'aide de ciseaux de cuisine, découpez le poulet le long de la colonne vertébrale pour la retirer. Ouvrez le poulet à plat et appuyez fermement sur le bréchet pour le surélever et l'aplatir complètement.
2. **L'assaisonnement :** Badigeonnez tout le poulet d'huile d'olive. Mélangez le paprika, l'ail et le sel, puis frottez généreusement l'ensemble du poulet avec ce mélange.
3. **Le chargement :** Remplis la boîte de fumage située sur le côté avec ton gobelet de pellets.
4. **La configuration :** Sélectionnez la fonction **ROAST**, réglez la température sur **190°C** et le temps sur **45 minutes**. **Activez impérativement le bouton WOODFIRE FLAVOR**. Lancez le préchauffage.
5. **La cuisson :** Au signal, déposez le poulet bien à plat sur la grille, côté peau vers le haut. Fermez le couvercle. Laissez cuire jusqu'à ce que la peau soit bien dorée et croustillante. Vérifiez avec votre application Connect : la température au cœur de la cuisse doit atteindre 75°C.

## 💡 Notes & Astuces
- Évitez d'ouvrir le couvercle durant les 30 premières minutes pour garder toute la fumée du Woodfire concentrée sur la viande.

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