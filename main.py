import cv2
import math
import mediapipe as mp
import time
from playsound import playsound
from pygame import mixer





def distance(p1, p2):
    x1 = p1
    x2 = p2
    dist = math.sqrt((x1 - x2)**2)
    return dist

if __name__ == '__main__':

    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_face_mesh = mp.solutions.face_mesh

    drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
    cap = cv2.VideoCapture(0)


    with mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as face_mesh:
        while cap.isOpened():
            success, image = cap.read()
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)



            imgH, imgW, _ = image.shape

            # Left eye indexes: P1 = 385, P2 = 387, P3 = 380, P4 = 373
            # Right eye: P1 = 160, P2 = 158, P3 = 144, P4 = 153


            leftEye = [[results.multi_face_landmarks[0].landmark[385].x * imgW, results.multi_face_landmarks[0].landmark[385].y * imgH],
                       [results.multi_face_landmarks[0].landmark[387].x * imgW, results.multi_face_landmarks[0].landmark[387].y * imgH],
                       [results.multi_face_landmarks[0].landmark[380].x * imgW, results.multi_face_landmarks[0].landmark[380].y * imgH],
                       [results.multi_face_landmarks[0].landmark[373].x * imgW, results.multi_face_landmarks[0].landmark[373].y * imgH]]

            rightEye = [[results.multi_face_landmarks[0].landmark[160].x * imgW, results.multi_face_landmarks[0].landmark[160].y * imgH],
                       [results.multi_face_landmarks[0].landmark[158].x * imgW, results.multi_face_landmarks[0].landmark[158].y * imgH],
                       [results.multi_face_landmarks[0].landmark[144].x * imgW, results.multi_face_landmarks[0].landmark[144].y * imgH],
                       [results.multi_face_landmarks[0].landmark[153].x * imgW, results.multi_face_landmarks[0].landmark[153].y * imgH],]


            dist1 = distance(leftEye[0][1], leftEye[2][1])
            dist2 = distance(leftEye[1][1], leftEye[3][1])

            dist3 = distance(rightEye[0][1], rightEye[2][1])
            dist4 = distance(rightEye[1][1], rightEye[3][1])

            if dist1 and dist2 < 1.5:
                leftEyeState = 'closed'
            else:
                leftEyeState = 'opened'

            if dist3 and dist4 < 1.5:
                rightEyeState = 'closed'
            else:
                rightEyeState = 'opened'

            while(leftEyeState == 'opened' and rightEyeState == 'opened'):
                t1 = time.time()
                t2 = 0
                break

            while(leftEyeState == 'closed' and rightEyeState == 'closed'):
                t2 = time.time()
                break

            czas = t2-t1
            print(czas)

            mixer.init()
            sound = mixer.Sound('alarm.wav')

            while(czas > 2):
                #playsound(r'C:/Users/Maciek/Desktop/Sleepnt/alarm.mp3')
                sound.play()
                break

            cv2.imshow('MediaPipe Face Mesh', cv2.flip(image, 1))

            print(f'Left eye is {leftEyeState}, Right eye is {rightEyeState}')

            if cv2.waitKey(5) & 0xFF == 27:
                break
    cap.release()