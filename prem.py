import cv2
import cvzone
import mediapipe as md
from cvzone.PoseModule import PoseDetector
import numpy as np

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('D:\Exercise\suryanamaskar/video_suryanamaskar_3.mp4')#('D:/IMAGE/pushup/video_pushup_6.mp4')

detector = PoseDetector()
count = 0
stage =0
while True:
    _, img = cap.read()
    img = detector.findPose(img)
    lstlm , bbox = detector.findPosition(img, draw=False)

    if lstlm:
        angle1 = detector.findAngle(img,12,14,16) #RIGHT HAND
        angle2 = detector.findAngle(img,11,13,15) #LEFT HAND
        angle3 = detector.findAngle(img,24,26,28) #RIGHT LEG
        angle4 = detector.findAngle(img,23,25,27) #LEFT LEG
        angle5 = detector.findAngle(img,23,11,15) #LEFT HIP2WRIST
        angle6 = detector.findAngle(img,24,12,16) #RIGHT HIP2WRIST
        angle7 = detector.findAngle(img,25,23,11) #LEFT KNEE2SHOULDER
        angle8 = detector.findAngle(img,26,24,12) #RIGHT KNEE2SHOULDER
        angle11 = detector.findAngle(img,27,25,23) # LEFT LEG
        angle12 = detector.findAngle(img,28,26,24) # RIGHT LEG
        angle13 = detector.findAngle(img,25,23,15) # LEFT KNEE2WRIST
        angle14 = detector.findAngle(img,26,24,16) # RIGHT KNEE2WRIST
        angle16 = detector.findAngle(img,24,16,12) # RIGHT KNEE2SHOULDER
        angle16 = detector.findAngle(img,31,25,17) # LEFT TOE2KNEE2FINGER
        angle17 = detector.findAngle(img,32,26,18) # RIGHT TOE2KNEE2FINGER
        angle18 = detector.findAngle(img,15,13,11) # LEFT HAND
        angle19 = detector.findAngle(img,16,14,12) # RIGHT HAND
        angle20 = detector.findAngle(img,27,23,19) # LEFT LEG2HIP2FINGER
        angle21 = detector.findAngle(img,28,24,20) # RIGHT LEG2HIP2FINGER
        angle22 = detector.findAngle(img,27,25,28) # LEFT LEG2KNEE2LEG
        angle23 = detector.findAngle(img,28,26,27) # RIGHT LEG2KNEE2LEG

        per = int(np.interp(angle1, (90, 160), (0, 100)))
        bar = int(np.interp(angle1, (0, 100), (80 + 400, 80)))

        cv2.rectangle(img, (590, bar), ((590 + 35), (80 + 400)), (0, 0, 255), cv2.FILLED)
        cv2.rectangle(img, (590, 80), ((590 + 35), (80 + 400)), (), 3)
        cvzone.putTextRect(img, f'{per} %', (580, 70), 1, 2, colorT=(255, 255, 255), colorR=(0, 0, 255), border=2,
                           colorB=())

        if angle3 > 160 and angle3 < 180 or angle4 > 160 and angle4 < 180:
            if angle1 > 280 and angle1 <= 330 or angle2 > 280 and angle2 <= 330:
                if angle18 > 20 and angle18 < 60 or angle19 > 20 and angle19 < 60:
                    if angle20 > 160 and angle20 < 180 or angle21 > 160 and angle21 < 180:
                        stage = "First1"
                        count = 1
        if stage == 'First1':
            if angle5 > 200 and angle5 <= 210 or angle6 > 200 and angle6 <= 210 :
                if angle1 > 190 and angle1 <= 250 or angle2 > 190 and angle2 <= 250:
                    stage = "Second2"
                    count = 2
        if stage == 'Second2':
            if angle7 > 20 and angle7 <= 50 or angle8 > 20 and angle8 <= 50 :
                stage = "Third3"
                count = 3
        if stage == 'Third3':
            if angle3 > 100 and angle3 <= 135 or angle4 > 100 and angle4 <= 135:
                stage = "Four4"
                count = 4
        if stage == 'Four4':
            if angle5 > 160 and angle5 <= 190 or angle6 > 160 and angle6 <= 190 :
                if angle11 > 160 and angle11 <= 190 or angle12 > 160 and angle12 <= 190:
                    stage = "Five5"
                    count = 5
        if stage == 'Five5':
            if angle16 > 150 and angle16 <= 190 or angle17 > 150 and angle17 <= 190 :
                if angle7 > 100 and angle8 < 150 or angle7 > 100 and angle8 < 150:
                    stage = "Six6"
                    count = 6
        if stage == 'Six6':
            if angle13 > 120 and angle13 <= 160 or angle14 > 120 and angle14 <= 160:
                stage = "Seven7"
                count = 7
        if stage == 'Seven7':
            if angle5 > 160 and angle5 <= 190 or angle6 > 160 and angle6 <= 190 :
                if angle11 > 160 and angle11 <= 190 or angle12 > 160 and angle12 <= 190:
                    stage = "Eight8"
                    count = 8
        if stage == 'Eight8':
            if angle3 > 100 and angle3 <= 135 or angle4 > 100 and angle4 <= 135:
                if angle22 > 160 and angle22 <= 200 or angle23 > 160 and angle23 <= 200:
                    stage = "Nine9"
                    count = 9
        if stage == 'Nine9':
            if angle7 > 20 and angle7 <= 50 or angle8 > 20 and angle8 <= 50 :
                if angle3 > 160 and angle4 <= 190 or angle3 > 160 and angle4 <= 190:
                    stage = "Ten10"
                    count = 10
        if stage == 'Ten10':
            if angle5 > 200 and angle5 <= 210 or angle6 > 200 and angle6 <= 210 :
                if angle1 > 190 and angle1 <= 250 or angle2 > 190 and angle2 <= 250:
                    stage = "Eleven11"
                    count = 11
        if stage == 'Eleven11':
            if angle3 > 160 and angle3 < 180 or angle4 > 160 and angle4 < 180:
                if angle1 > 280 and angle1 <= 330 or angle2 > 280 and angle2 <= 330:  
                    stage = "Twelve12"
                    count = 12
                    
        print(count)

    cv2.putText(img, 'REPS', (15, 12),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
    cvzone.putTextRect(img,str(count), (10,60), 1, 2, colorT=(255, 255, 255), colorR=(0, 0, 255), border=2,
                       colorB=())

    cv2.imshow("Push-UP Counter",img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
