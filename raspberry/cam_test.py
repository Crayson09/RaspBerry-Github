import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob

# Konstanten
COLOR_FACE = (255, 0, 255)  # Farbe für Rahmen ums Gesicht (Magenta)
SIMILARITY_THRESHOLD = 0.8  # Schwellenwert für die Ähnlichkeitsbewertung

# Liste der Bilddateien im aktuellen Verzeichnis
image_files = glob.glob("*.jpg")
# Referenzbild der gesuchten Person (Beispiel: Muss angepasst werden)
reference_image = cv2.imread('reference.jpg', cv2.IMREAD_COLOR)
reference_gray = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)

# Dimensionen des Referenzgesichts
(rw, rh) = reference_gray.shape[::-1]

# Initiiere den Gesichtserkennungsklassifikator
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Für jedes Bild Gesichtserkennung durchführen
for file in image_files:
    # Bild einlesen und vorbereiten
    img_bgr = cv2.imread(file, cv2.IMREAD_COLOR)
    b, g, r = cv2.split(img_bgr)
    img_rgb = cv2.merge([r, g, b])
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # Gesichter im aktuellen Bild erkennen
    faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.2, minNeighbors=5)

    print(f"Anzahl erkannte Gesichter in {file}: {len(faces)}")

    # Liste für ausgeschnittene Gesichter
    cropped_faces = []

    # Gesichter ausschneiden und in Liste speichern
    for (x, y, w, h) in faces:
        face = img_rgb[y:y+h, x:x+w]

        # Gesicht auf die Größe des Referenzgesichts skalieren
        scaled_face = cv2.resize(face, (rw, rh))

        cropped_faces.append(scaled_face)

    # Vergleich der ausgeschnittenen Gesichter mit Referenzgesicht
    if len(reference_gray) > 0:
        for face in cropped_faces:
            # Berechnung der Ähnlichkeit (Mittlerer quadratischer Fehler)
            mse = np.mean((reference_gray - cv2.cvtColor(face, cv2.COLOR_BGR2GRAY))**2)
            similarity_score = 1 / (1 + mse)  # Höherer Wert bedeutet höhere Ähnlichkeit

            # Ausgabe der Ähnlichkeit und Anzeige des Bildes mit markiertem Gesicht
            if similarity_score > SIMILARITY_THRESHOLD:
                print(f"Ähnlichkeit mit der gesuchten Person gefunden in {file}!")
                plt.axis('off')
                plt.imshow(cv2.cvtColor(face, cv2.COLOR_BGR2RGB))
                plt.title(f"Gesicht in {file}")
                plt.show()
                break  # Nur das erste passende Gesicht anzeigen

    # Anzeigen des Bildes mit markierten Gesichtern (ohne Ähnlichkeitsprüfung)
    for (x, y, w, h) in faces:
        cv2.rectangle(img_rgb, (x, y), (x + w, y + h), COLOR_FACE, 2)

    plt.axis('off')
    plt.imshow(img_rgb)
    plt.title(file)
    plt.show()

print("Programm beendet.")
