# OPEN CV example
import cv2
import mediapipe as mp
print(mp.__file__)
import pyautogui
# capture cam
cam = cv2.VideoCapture(0)
#
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

while True:
    # read each frame
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmarks_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape

    if landmarks_points:
        landmarks = landmarks_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
                screen_x = screen_w / frame_w * x
                screen_y = screen_h / frame_h * y
                pyautogui.moveTo(screen_x, screen_y)
        left = [landmarks[145], landmarks[159]]
        right = [landmarks[374], landmarks[386]]
        mouth = [landmarks[14], landmarks[13]]

        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))

        for landmark in right:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (255, 255, 0))

        # Marks de la boca
        for landmark in mouth:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (255, 0, 0))

        if (left[0].y - left[1].y) < 0.004:
            pyautogui.click(button='right')
            pyautogui.sleep(1)

        if (right[0].y - right[1].y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(1)

        #print(mouth[0].y - mouth[1].y)
        if (mouth[0].y - mouth[1].y) > 0.0065:
            #print(mouth[0].y - mouth[1].y)
            pyautogui.doubleClick()
            pyautogui.sleep(1)

    cv2.imshow('Eye Controller', frame)
    cv2.waitKey(1)
