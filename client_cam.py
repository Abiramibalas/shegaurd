import cv2
import requests
import time

CENTRAL_SERVER_URL = 'http://192.168.236.174:5020/receive_feed'  # Replace with Laptop Z IP
CAM_ID = 'laptop_c'  # Change this per laptop
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    _, img_encoded = cv2.imencode('.jpg', frame)
    response = requests.post(
        CENTRAL_SERVER_URL,
        files={'image': img_encoded.tobytes()},
        data={'source': CAM_ID}
    )

    time.sleep(0.01)# ~10 FPS