# 🍣 Sushis et Makis Maison

> Une recette testée et approuvée, idéale pour recevoir. Le secret réside dans la préparation du riz et la patience !

| Préparation | Repos | Cuisson | Portions |
| :--- | :--- | :--- | :--- |
| 45 min | 50 min | 20 min | <input type="number" id="servings" value="8" min="1" style="width: 50px; font-weight: bold;"> rouleaux |

## 🛠 Matériel nécessaire
- [ ] Cuiseur à riz (Rice cooker)
- [ ] Natte en bambou (plus efficace que le silicone)
- [ ] Récipient non métallique (plat en bois ou plateau-repas)

## 🛒 Ingrédients

### Le Riz (Base)
- [ ] <span class="qty" data-base="500">500</span> g de riz à sushi/maki
- [ ] <span class="qty" data-base="625">625</span> ml d'eau
- [ ] <span class="qty" data-base="105">105</span> ml de vinaigre de riz
- [ ] <span class="qty" data-base="55">55</span> g de sucre
- [ ] <span class="qty" data-base="0.5">0.5</span> cuillère à café de sel

### Garnitures (Makis)
- [ ] <span class="qty" data-base="8">8</span> à 9 feuilles d'algues Nori
- [ ] <span class="qty" data-base="300">300</span> g de saumon frais (qualité sashimi)
- [ ] <span class="qty" data-base="250">250</span> g de crevettes (ouvertes et nettoyées)
- [ ] <span class="qty" data-base="1">1</span> avocat
- [ ] <span class="qty" data-base="1">1</span> concombre
- [ ] <span class="qty" data-base="0.5">0.5</span> carotte
- [ ] <span class="qty" data-base="1">1</span> pot de fromage frais (type Philadelphia)

### Accompagnements
- [ ] Graines de sésame
- [ ] Gingembre (confit ou frais)
- [ ] Wasabi et Piment
- [ ] Sauce soja salée

## 🥣 Instructions

### 1. Préparation du riz
1. **Lavage :** Laver le riz dans le récipient du cuiseur 3 ou 4 fois, jusqu'à ce que l'eau soit bien claire.
2. **Repos 1 :** Laisser reposer le riz dans une passoire pendant **30 minutes**.
3. **Cuisson :** Mettre le riz et les 625 ml d'eau dans le cuiseur. Lancer la cuisson.
4. **Repos 2 :** Une fois que le cuiseur passe en mode "chaud" (après environ 15-20 min), laisser le riz reposer encore quelques minutes.

### 2. L'assaisonnement (Le Su)
1. Mélanger le vinaigre de riz, le sucre et le sel. 
2. **Astuce :** Passer le mélange 1 minute au micro-ondes pour faciliter la dissolution du sucre et adoucir le vinaigre.
3. Transférer le riz cuit dans un récipient **non métallique**.
4. Verser le mélange de vinaigre sur le riz et mélanger délicatement sans écraser les grains.
5. Laisser tiédir à température ambiante (ne pas mettre au frigo).

### 3. Montage
1. Découper le poisson et les légumes en bâtonnets fins.
2. Placer une feuille d'algue sur la natte en bambou.
3. Étaler le riz tiède (s'il est trop chaud, l'algue fane ; trop froid, il ne colle plus).
4. Ajouter la garniture et rouler fermement avec la natte.

## 💡 Notes & Astuces
* **Test de température :** Le riz doit être à température corporelle pour une manipulation optimale.
* **Persévérance :** C'est au bout de quelques essais que l'on prend vraiment la main sur le roulage.
* **Tutos :** N'hésitez pas à regarder une vidéo pour la technique de découpe et de roulage des makis.

---
[⬅ Retour à l'index](../README.md)

<script>
  const servingInput = document.getElementById('servings');
  const baseServings = 8;

  servingInput.addEventListener('input', () => {
    const ratio = servingInput.value / baseServings;
    document.querySelectorAll('.qty').forEach(span => {
      const baseValue = parseFloat(span.getAttribute('data-base'));
      let newValue = Math.round((baseValue * ratio) * 10) / 10;
      span.textContent = newValue;
    });
  });
</script>