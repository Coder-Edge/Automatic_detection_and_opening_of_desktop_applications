import time
import cv2
import numpy as np
import pyautogui
import os

# Configuration
CHEMIN_IMAGE_CHROME = "./images/Chrome.png"  # Modifier si nécessaire
SEUIL_CONFIANCE = 0.5  # Seuil de confiance (0 = faible, 1 = strict)

def capture_bureau_seul():
    """Capture une image du bureau Windows après avoir réduit toutes les fenêtres."""
    print("📷 Capture du bureau...")

    # Réduire toutes les fenêtres
    pyautogui.hotkey('win', 'd')
    time.sleep(2)

    # Capture d'écran
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Restaurer les fenêtres
    # pyautogui.hotkey('win', 'd')
    time.sleep(1)

    return screenshot

def detecter_chrome(image, chemin_template, seuil):
    """Détecte l'icône Chrome sur le bureau avec le template fourni.
    Retourne un tuple: (image_annotée, x_centre, y_centre, détection_réussie)"""
    if not os.path.exists(chemin_template):
        print(f"⚠ Fichier image introuvable : {chemin_template}")
        return image, None, None, False

    template = cv2.imread(chemin_template)
    if template is None:
        print("⚠ Impossible de charger le fichier template.")
        return image, None, None, False

    template = cv2.resize(template, (50, 50))  # Redimensionner si nécessaire
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val >= seuil:
        h, w = template.shape[:2]
        x, y = max_loc
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, f"App ({x}, {y})", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        print(f"✅  Appli détecté à ({x}, {y}) - Confiance : {max_val:.2f}")
        centre_x, centre_y = x + (w // 2), y + (h // 2)
        return image, centre_x, centre_y, True
    else:
        print(f"❌ Appli non détecté - Meilleure confiance : {max_val:.2f}")
        return image, None, None, False

def open_app(x, y):
    """Ouvre l'application en cliquant sur ses coordonnées."""
    if x is None or y is None:
        return False
        
    # Déplacement et double clic
    pyautogui.moveTo(x, y, duration=0.5)  # 0.5s de mouvement fluide
    pyautogui.doubleClick()
    return True

def main():
    # Étape 1 : Capture
    bureau = capture_bureau_seul()

    # Étape 2 : Détection
    image_resultat, x, y, detection_ok = detecter_chrome(bureau.copy(), CHEMIN_IMAGE_CHROME, SEUIL_CONFIANCE)

    # Étape 3 : Sauvegarde du résultat
    cv2.imwrite('resultat_app.png', image_resultat)
    
    # Étape 4 : Ouverture de l'application si détectée
    if detection_ok:
        if open_app(x, y):
            print("✅ Application ouverte avec succès.")
        else:
            print("❌ Échec de l'ouverture de l'application.")
    else:
        print("❌ Impossible d'ouvrir l'application car elle n'a pas été détectée.")

if __name__ == "__main__":
    main()