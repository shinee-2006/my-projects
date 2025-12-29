import cv2
import mediapipe as mp
import requests
import time

ESP32_IP = "http://192.168.4.1"
SEND_DELAY = 0.7

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

last_command = ""
last_time = time.time()

tip_ids = [4, 8, 12, 16, 20]

def send_command(cmd):
    global last_command, last_time
    current_time = time.time()
    if cmd != last_command and (current_time - last_time) > SEND_DELAY:
        try:
            requests.get(f"{ESP32_IP}/{cmd}", timeout=0.3)
            print("Sent command:", cmd)
            last_command = cmd
            last_time = current_time
        except:
            print("ESP32 not reachable")

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    finger_count = 0

    if result.multi_hand_landmarks:
        hand_landmarks = result.multi_hand_landmarks[0]
        lm = hand_landmarks.landmark

        if lm[tip_ids[0]].x < lm[tip_ids[0] - 1].x:
            finger_count += 1

        for i in range(1, 5):
            if lm[tip_ids[i]].y < lm[tip_ids[i] - 2].y:
                finger_count += 1

        mp_draw.draw_landmarks(
            img, hand_landmarks, mp_hands.HAND_CONNECTIONS
        )

    if finger_count == 1:
        send_command("one")
        action = "FORWARD"
    elif finger_count == 2:
        send_command("two")
        action = "BACKWARD"
    elif finger_count == 3:
        send_command("three")
        action = "LEFT"
    elif finger_count == 4:
        send_command("four")
        action = "RIGHT"
    else:
        send_command("stop")
        action = "STOP"

    cv2.putText(
        img,
        f"Fingers: {finger_count} | Action: {action}",
        (10, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 255, 0),
        2
    )

    cv2.imshow("Hand Gesture Control", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
