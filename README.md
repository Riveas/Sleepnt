# Sleepnt - app that won't let you fall asleep
Sleepnt is a simple app written entirely in python that might come handy when the deadline is tight and day is short. 
Main usage of the app would be to prevent falling asleep when there's still some things to do but all you can think of is falling asleep. 
With this project every time you'll start snoozing, you'll be reminded with sound alarm that it's not time for sleeping yet.
## Required modules:
* OpenCV
* Mediapipe
* Pygame
* Math
* Time
## Installation guide:
To ensure that your project will work fine first you'll need to install necessary modules. You can do it simply by running following commands in your terminal:
pip install opencv-python  
pip install mediapipe  
pip install pygame  
## Setup
First thing to do is initiating opencv and mediapipe facial recognition model
```
    mp_face_mesh = mp.solutions.face_mesh

    cap = cv2.VideoCapture(0)
```
Then you'll need to setup your model
```
    with mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as face_mesh:
```
Next you'll want to start your webcam and process image by mediapipe model
```
        while cap.isOpened():
            success, image = cap.read()
            results = face_mesh.process(image)
```
What you get as a result of processing your image is list containing 468 landmarks, each having their x,y and z position in image.
For analysing your eye you'll need 8 landmarks seen as below:  
![eyes](https://user-images.githubusercontent.com/130605144/232501991-340835ef-d372-483a-ba7f-44d2cdd64f48.png)  
Points indices: P1 = 385, P2 = 387, P3 = 380, P4 = 373, P5 = 160, P6 = 158, P7 = 144, P8 = 153  
To detect whether eyes are opened or closed you can calculate the distance between top and bottom pair of points. To do so you can simply calculate euclidean distance: 
```
    def distance(p1, p2):
        x1 = p1
        x2 = p2
        dist = math.sqrt((x1 - x2)**2)
        return dist
```
Next step in your project is extracting x and y values from results list:
```
            leftEye = [[results.multi_face_landmarks[0].landmark[385].x * imgW, results.multi_face_landmarks[0].landmark[385].y * imgH],
                       [results.multi_face_landmarks[0].landmark[387].x * imgW, results.multi_face_landmarks[0].landmark[387].y * imgH],
                       [results.multi_face_landmarks[0].landmark[380].x * imgW, results.multi_face_landmarks[0].landmark[380].y * imgH],
                       [results.multi_face_landmarks[0].landmark[373].x * imgW, results.multi_face_landmarks[0].landmark[373].y * imgH]]

            rightEye = [[results.multi_face_landmarks[0].landmark[160].x * imgW, results.multi_face_landmarks[0].landmark[160].y * imgH],
                       [results.multi_face_landmarks[0].landmark[158].x * imgW, results.multi_face_landmarks[0].landmark[158].y * imgH],
                       [results.multi_face_landmarks[0].landmark[144].x * imgW, results.multi_face_landmarks[0].landmark[144].y * imgH],
                       [results.multi_face_landmarks[0].landmark[153].x * imgW, results.multi_face_landmarks[0].landmark[153].y * imgH],
```
To detect whether eye is opened or not you'll only need the y variable but for debugging purpose x variable was also extracted.  
Once you have your y variable extracted you can calculate euclidean distance:
```
            dist1 = distance(leftEye[0][1], leftEye[2][1])
            dist2 = distance(leftEye[1][1], leftEye[3][1])

            dist3 = distance(rightEye[0][1], rightEye[2][1])
            dist4 = distance(rightEye[1][1], rightEye[3][1])
```
