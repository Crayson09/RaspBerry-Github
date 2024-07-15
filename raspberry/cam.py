import cv2
import subprocess
import numpy as np

# Funktion zum Erfassen eines Bildes mit libcamera
def capture_image():
    # Führen Sie libcamera-Command aus, um ein Bild aufzunehmen
    subprocess.run(["libcamera-still", "-o", "image.jpg", "--nopreview"])

    # Lesen Sie das aufgenommene Bild ein
    image = cv2.imread("image.jpg")
    return image

# Gesichtserkennung mit OpenCV
def detect_faces(image):
    # Laden Sie den vortrainierten Haar-Cascade-Klassifikator
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Konvertieren Sie das Bild in Graustufen
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Erkennen Sie Gesichter
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

def main():
    # Erfassen Sie ein Bild
    image = capture_image()

    # Erkennen Sie Gesichter im Bild
    faces = detect_faces(image)

    # Zeichnen Sie Rechtecke um erkannte Gesichter
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Anzeigen des Bildes mit erkannten Gesichtern
    cv2.imshow('Image with Faces', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
