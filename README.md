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
