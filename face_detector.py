import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

if cap.isOpened():
    while True:
        ret, frame = cap.read()

        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            cv2.imshow("Faces", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            if cv2.getWindowProperty("Faces", cv2.WND_PROP_VISIBLE) < 1:
                break

        else:
            break

cap.release()
cv2.destroyAllWindows()


# import cv2
# import mediapipe as mp

# # Load Face Detection Cascade
# face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# # Initialize MediaPipe Face Mesh
# mp_face_mesh = mp.solutions.face_mesh
# face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=2, min_detection_confidence=0.5)

# # Initialize MediaPipe Hand Detection
# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# # Video Capture
# cap = cv2.VideoCapture(0)

# if cap.isOpened():
#     while True:
#         ret, frame = cap.read()

#         if ret:
#             # Convert to Grayscale
#             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#             # Face Detection
#             faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

#             # Face Mesh Detection
#             results = face_mesh.process(frame)
#             if results.multi_face_landmarks:
#                 for face_landmarks in results.multi_face_landmarks:
#                     # Render face mesh
#                     # Use face_landmarks to draw mesh on the frame
#                     pass  # Your code to render face mesh goes here

#             # Hand Detection and Finger Tracking
#             results_hands = hands.process(frame)
#             if results_hands.multi_hand_landmarks:
#                 for hand_landmarks in results_hands.multi_hand_landmarks:
#                     # Render hand landmarks
#                     # Use hand_landmarks to track fingers and draw them on the frame
#                     pass  # Your code to track fingers and render them goes here

#             # Display the frame
#             cv2.imshow("Faces", frame)

#             # Break the loop if 'q' is pressed
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break

#             # Break the loop if the window is closed
#             if cv2.getWindowProperty("Faces", cv2.WND_PROP_VISIBLE) < 1:
#                 break

#         else:
#             break

# # Release Video Capture and Close Windows
# cap.release()
# cv2.destroyAllWindows()
