import cv2
import mediapipe as mp
import time

import HandTrackingModule as htm


pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Set width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Set height
detector = htm.HandDetector(mode=False, maxHand=2, mc=1, detectionCon=0.3, trackCon=0.3)

while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=False )
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        print(lmList[4])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)