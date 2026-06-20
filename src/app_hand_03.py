import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
draw_utils = mp.solutions.drawing_utils

draw_utils = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)


finger_counetr = 0



while True:
   
    success , frame  = cap.read(0)
    if not success:
        break
    finger_counetr = 0
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frameRGB)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:

            landmarks = hand.landmark
            finger_tip = [8, 12, 16, 20]
            for tip in finger_tip:
                if landmarks[tip].y < landmarks[tip - 2].y:
                    finger_counetr += 1
            if landmarks[4].x > landmarks[3].x:
                finger_counetr += 1



            draw_utils.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

    cv2.putText(frame, str(finger_counetr), (50, 100), cv2.FONT_HERSHEY_SIMPLEX,3, 
                 (0, 255, 0), 3)
    
    cv2.imshow('CAMERA', frame)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()