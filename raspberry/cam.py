from picamera2 import Picamera2, Preview
from time import sleep

picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start_preview(Preview.QTGL)
picam2.start()
sleep(2)
picam2.capture_file("test.jpg")
