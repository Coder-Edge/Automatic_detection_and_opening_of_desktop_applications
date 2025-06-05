
# 📂 Projet : Détection et ouverture automatique d'une application sur le bureau (ex. Chrome)

Ce script Python permet de **détecter visuellement une icône d'application sur le bureau Windows** (comme celle de Google Chrome), puis de **la lancer automatiquement par double-clic**, en combinant des techniques de vision par ordinateur et d'automatisation.

## 🚀 Fonctionnalités

- 🖼️ Capture automatique du bureau (réduction temporaire des fenêtres ouvertes)
- 🔍 Détection d'une icône à l'écran via `cv2.matchTemplate` (template matching)
- ✅ Annoter et sauvegarder l'image avec la position détectée
- 🖱️ Simulation d’un double-clic pour lancer l'application détectée
- 🛠️ Modifiable pour détecter n'importe quelle autre application (changer le template)

## 🛠️ Technologies utilisées

- `OpenCV` pour la vision par ordinateur
- `PyAutoGUI` pour contrôler la souris et le clavier
- `NumPy` pour la manipulation d’image
- `time` et `os` pour la gestion système

## 🖼️ Pré-requis

- Windows (utilise le raccourci `Win + D`)
- Python 3.x
- Fichier image `.png` de l’icône à détecter (ex: `./images/Chrome.png`)

## 🔧 Installation

```bash
pip install opencv-python pyautogui numpy
```

## 📦 Utilisation

1. Place l’icône cible dans un dossier `./images/` sous le nom `Chrome.png`
2. Lance le script :

```bash
python detecteur_lanceur.py
```

3. Le programme :
   - capture le bureau
   - cherche l’icône dans la capture
   - la surligne si trouvée
   - et fait un **double-clic automatique** dessus

## 📸 Exemple de sortie

- `resultat_app.png` : une capture annotée de la détection
- Console :
  ```
  📷 Capture du bureau...
  ✅  Appli détecté à (1432, 820) - Confiance : 0.76
  ✅ Application ouverte avec succès.
  ```

## ✅ À adapter

- Pour ouvrir une autre application : remplace `./images/Chrome.png` par une image de ton choix.
- Ajuste la variable `SEUIL_CONFIANCE` si l’icône est mal reconnue ou trop sensible.