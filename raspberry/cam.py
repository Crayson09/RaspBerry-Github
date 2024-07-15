import cv2
import glob
import matplotlib
matplotlib.use('Agg')  # Verwendung eines nicht-interaktiven Backends für matplotlib
from matplotlib import pyplot as plt
import foto  # Annahme, dass 'foto' ein eigenes Modul ist, das die Kamerafunktionalität enthält

COLOR_FACE = (255, 0, 255)  # Farbe für Rahmen ums Gesicht (Magenta)

# Funktion zum Aufnehmen eines Fotos
def take_photo():
    foto.foto()

# Hauptprogramm für Gesichtserkennung
def main():
    take_photo()  # Foto aufnehmen (muss die Foto-Funktion entsprechend implementieren)

    image_files = glob.glob("*.jpg")  # Alle jpg-Dateien im aktuellen Verzeichnis in Liste speichern

    # Für jedes Bild Gesichtserkennung machen
    for file in image_files:
        img_bgr = cv2.imread(file, cv2.IMREAD_COLOR)  # Die Bilddatei farbig einlesen
        b, g, r = cv2.split(img_bgr)  # Die Farbwerte auslesen (cv2 erstellt BGR-Bild)
        img_rgb = cv2.merge([r, g, b])  # Aus den BGR-Farbwerten ein RGB-Bild machen
        img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)  # Ein Graustufenbild für die Erkennung machen

        # Gesichts-Klassifikatoren aus Datei laden
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        # Eigentliche Gesichtserkennung ausführen
        faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.2, minNeighbors=5)

        print("Anzahl erkannte Gesichter:", len(faces))  # Anzahl erkannte Gesichter ausgeben

        # Erkannte Gesichter durchgehen und markieren
        for (x, y, w, h) in faces:
            cv2.rectangle(img_rgb, (x, y), (x + w, y + h), COLOR_FACE, 2)  # Gesichter mit Rahmen markieren

        # Bild anzeigen und speichern
        plt.figure(figsize=(8, 6))
        plt.axis('off')
        plt.imshow(img_rgb)
        plt.title(file)
        plt.savefig('marked_' + file + '.png')  # Bild speichern
        plt.close()

    exit()  # Beendet das Programm nach der Verarbeitung der Bilder

if __name__ == "__main__":
    main()
