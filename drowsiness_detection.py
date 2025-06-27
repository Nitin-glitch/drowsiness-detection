import cv2
import dlib
from scipy.spatial import distance
import winsound  # For Windows alert sound (alternatively use playsound for other OS)

def calculate_EAR(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Load face detector and shape predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Start webcam
cap = cv2.VideoCapture(0)

# Eye landmarks
LEFT_EYE = list(range(36, 42))
RIGHT_EYE = list(range(42, 48))

# EAR Threshold and Score
EAR_THRESHOLD = 0.25
SCORE = 0

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        shape = predictor(gray, face)
        shape = [(shape.part(i).x, shape.part(i).y) for i in range(68)]

        left_eye = [shape[i] for i in LEFT_EYE]
        right_eye = [shape[i] for i in RIGHT_EYE]

        left_ear = calculate_EAR(left_eye)
        right_ear = calculate_EAR(right_eye)
        ear = (left_ear + right_ear) / 2.0

        if ear < EAR_THRESHOLD:
            SCORE += 1
            if SCORE > 15:
                cv2.putText(frame, "DROWSINESS ALERT!", (20, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
                winsound.Beep(1000, 1000)  # Frequency, Duration
        else:
            SCORE = 0

        cv2.putText(frame, f"EAR: {ear:.2f}", (20, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Drowsiness Detection", frame)
    if cv2.waitKey(1) == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()