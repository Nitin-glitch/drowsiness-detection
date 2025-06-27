# Real-Time Driver Drowsiness Detection System

## Overview
This project detects drowsiness in real-time using a webcam feed by analyzing the Eye Aspect Ratio (EAR) using facial landmarks. It alerts the driver using sound when signs of fatigue are detected.

## Technologies Used
- Python
- OpenCV
- dlib
- scipy
- winsound (for Windows sound alert)

## Setup Instructions
1. Clone the repository or download the files.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the shape predictor model:
   [Download from Dlib Website](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)
   Extract it and place `shape_predictor_68_face_landmarks.dat` in the project folder.

4. Run the application:
   ```bash
   python drowsiness_detection.py
   ```

## Features
- Real-time video capture from webcam
- Eye Aspect Ratio (EAR) computation
- Drowsiness scoring logic
- Audio alert if drowsiness threshold is exceeded

## Output Sample and Eye Aspect Ratio Graph Changes
https://github.com/user-attachments/assets/5ca66b33-d3b2-4d4a-84ad-c6c5d2afb9d3

## Future Scope
- Add yawn detection and head tilt monitoring
- Port to Raspberry Pi for embedded deployment
- Integrate with smart vehicles for automatic control

## Author
Nitin Chourasia
