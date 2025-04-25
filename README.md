# **Fruit Capture Game 🍎👋**  

**Un jeu interactif contrôlé par les mouvements de la main, utilisant Python, MediaPipe et Pygame.**  

## 📌 **Description**  
Ce projet est un **jeu de capture de fruits** où vous contrôlez un curseur avec votre main via la webcam. Le but est d'attraper les fruits qui tombent en **pointant avec votre index** pour marquer des points avant la fin du temps imparti.  

### **Fonctionnalités**  
✅ **Détection des mains en temps réel** avec **MediaPipe**  
✅ **Contrôle gestuel** (déplacement et pointage)  
✅ **Système de score et chronomètre**  
✅ **Effets visuels** (rotation des fruits, feedback de capture)  
✅ **Structure modulaire** pour une maintenance facile  

---

## 🛠 **Technologies utilisées**  
- **Python** 🐍  
- **Pygame** (pour le rendu graphique)  
- **MediaPipe** (détection des mains et gestes)  
- **OpenCV** (traitement du flux vidéo)  

---

## 🚀 **Installation & Exécution**  

### **Prérequis**  
- Python 3.8+  
- Une webcam fonctionnelle  

### **1. Clonez le dépôt**  
```bash
git clone https://github.com/votre-utilisateur/fruit-capture-game.git
cd fruit-capture-game
```

### **2. Installez les dépendances**  
```bash
pip install -r requirements.txt
```

### **3. Lancez le jeu**  
```bash
python main.py
```

### **🎮 Comment jouer ?**  
- **Déplacez votre main** devant la caméra pour bouger le curseur.  
- **Pointez avec l'index** pour capturer les fruits.  
- **Appuyez sur ESPACE** pour recommencer.  
- **ÉCHAP** pour quitter.  

---

## 📂 **Structure du projet**  
```
fruit-capture-game/  
├── main.py            # Point d'entrée principal  
├── settings.py        # Configuration du jeu  
├── hand_controller.py # Détection des mains (MediaPipe)  
├── game_object.py     # Gestion des fruits  
├── game_ui.py         # Interface utilisateur  
├── assets/            # Images et sons  
│   ├── 1-6.png       # Sprites des fruits  
│   ├── hand.png      # Curseur main normale  
│   ├── pic.png       # Curseur main pointante  
│   └── bg.jpeg       # Arrière-plan  
└── requirements.txt   # Dépendances  
```

---

## 📜 **Améliorations possibles**  
- [ ] Ajouter des **effets sonores**  
- [ ] Implémenter un **système de vies**  
- [ ] Créer des **niveaux de difficulté**  
- [ ] Ajouter un **mode multijoueur**  

---

## 🤝 **Contribuer**  
Les contributions sont les bienvenues !  
1. **Forkez** le projet  
2. Créez une branche (`git checkout -b feature/amelioration`)  
3. Committez (`git commit -m 'Ajout d'une fonctionnalité'`)  
4. Pushez (`git push origin feature/amelioration`)  
5. Ouvrez une **Pull Request**  

---

## 📄 **Licence**  
Ce projet est sous licence **MIT**.  

---

✨ **Amusez-vous bien !** ✨  

*N'hésitez pas à me contacter pour des questions ou des suggestions.* 🚀
