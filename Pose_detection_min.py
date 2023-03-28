import cv2
import mediapipe as mp
import time

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils


cam = cv2.VideoCapture(0)
ptime =0

while True:
    Success, img = cam.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = pose.process(imgRGB)
    # print(results.pose_landmarks)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            x,y,z = img.shape
            print(id,lm)
            cx , cy = int(lm.x*y), int(lm.y*x)

            cv2.circle(img, (cx,cy) , 7 ,(123,5,231), cv2.FILLED)



    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime =ctime

    cv2.putText(img, str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

    cv2.imshow("image",img)
    key = cv2.waitKey(1)& 0xff

    if key == ord('q'):
        break

