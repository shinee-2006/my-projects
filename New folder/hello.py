import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

tip_ids = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    finger_count = 0
    direction = "STOP"

    if result.multi_hand_landmarks:
        hand_landmarks = result.multi_hand_landmarks[0]
        lm = hand_landmarks.landmark

        if lm[tip_ids[0]].x < lm[tip_ids[0] - 1].x:
            finger_count += 1

        for i in range(1, 5):
            if lm[tip_ids[i]].y < lm[tip_ids[i] - 2].y:
                finger_count += 1

        mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    if finger_count == 1:
        direction = "FORWARD"
    elif finger_count == 2:
        direction = "BACK"
    elif finger_count == 3:
        direction = "LEFT"
    elif finger_count == 4:
        direction = "RIGHT"
    else:
        direction = "STOP"

    cv2.putText(
        img,
        f"Direction: {direction}",
        (30, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        3
    )

    cv2.imshow("Simple Hand Direction Detection", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
