import requests
import numpy as np
import cv2

while True:
    images = requests.get("http://192.168.43.1:8080/shot.jpg")
    video = np.array(bytearray(images.content), dtype=np.uint8)
    render = cv2.imdecode(video, -1)
    cv2.imshow('frame', render)
    if (cv2.waitKey(1)==ord('q')):
        break