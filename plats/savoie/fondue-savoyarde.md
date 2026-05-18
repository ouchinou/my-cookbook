# La Véritable Fondue Savoyarde aux Trois Fromages

> Le secret d'une fondue savoyarde réussie et inratable réside dans le choix et la proportion des fromages, ainsi que dans la maîtrise de la température pour éviter que le fromage ne file ou ne se sépare.

| Préparation | Cuisson | Portions |
| :--- | :--- | :--- |
| 15 min | 15 min | <input type="number" id="servings" value="4" min="1" style="width: 50px; font-weight: bold;"> pers. |

## 🛒 Ingrédients
- [ ] <span class="qty" data-base="300">300</span> g de Beaufort
- [ ] <span class="qty" data-base="300">300</span> g de Comté (de préférence fruité)
- [ ] <span class="qty" data-base="200">200</span> g d'Emmental de Savoie (ou d'Abondance)
- [ ] <span class="qty" data-base="30">30</span> cl de vin blanc sec de Savoie (ex: Apremont, Jacquère)
- [ ] <span class="qty" data-base="1">1</span> gousse d'ail
- [ ] <span class="qty" data-base="1">1</span> cuillère à café de fécule de maïs (Maïzena)
- [ ] <span class="qty" data-base="1">1</span> petit verre de Kirsch (optionnel)
- [ ] <span class="qty" data-base="1">1</span> pincée de noix de muscade râpée
- [ ] <span class="qty" data-base="1">1</span> pain de campagne de la veille (coupé en cubes)

## 🥣 Instructions
1. **La préparation :** Coupez le pain en cubes la veille ou quelques heures avant pour qu'il rassisse un peu (il tiendra mieux sur le pic). Râpez tous les fromages ou coupez-les en très petits dés.
2. **Le caquelon :** Épluchez la gousse d'ail, coupez-la en deux et frottez vigoureusement tout l'intérieur de votre caquelon. Laissez l'ail au fond.
3. **Le liant :** Dans un fond de verre, délayez la fécule de maïs dans le Kirsch (ou dans une cuillère de vin blanc). Ce petit mélange est l'ingrédient magique pour lier le fromage et le vin.
4. **La fonte :** Versez les 30 cl de vin blanc dans le caquelon et portez à ébullition à feu moyen. Dès que le vin frémit, baissez le feu et ajoutez le fromage poignée par poignée, en remuant sans arrêt avec une cuillère en bois en formant des "8". Attendez que la première poignée soit fondue avant d'en ajouter une autre.
5. **La liaison finale :** Une fois tout le fromage fondu et l'ensemble bien homogène, ajoutez la fécule délayée et la muscade. Laissez mijoter 1 à 2 minutes en remuant : la fondue devient alors bien crémeuse et veloutée. Transférez immédiatement sur le réchaud de table.

## 💡 Notes & Astuces
- **Le conseil "Inratable" :** Ne faites jamais bouillir le fromage ! Une chaleur trop intense sépare le gras de la protéine, ce qui crée une fondue "solide" qui baigne dans l'huile. On reste toujours sur un feu doux et une chaleur constante.

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