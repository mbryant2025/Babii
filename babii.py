import requests
import time
import picamera


with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)

    while True:
        camera.capture('image.jpg')

        with open("image.jpg", 'rb') as f:
            r = requests.post("https://www.babii.space/rpi/image", files={"image": f})

        time.sleep(5)