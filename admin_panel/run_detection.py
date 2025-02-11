import os
import cv2
from ultralytics import YOLO
from deepface import DeepFace
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail

# Set up Django project path
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin_panel.settings")  # Adjust 'admin_panel' to your Django project
import django
django.setup()  # Initialize Django

# Path configuration
yolov8_model_path = "C:/Users/dasvi/OneDrive/Desktop/Combine/yolov8nn.pt"
photos_folder = "C:/Users/dasvi/admin_panel/photos"

# Initialize models
model = YOLO(yolov8_model_path)

# Email settings
recipient_email = "dasviolina51@gmail.com"  # Replace with recipient's email

# Initialize webcam
cap = cv2.VideoCapture(0)

# Configuration constants
CONFIDENCE_THRESHOLD = 0.5
RECOGNITION_THRESHOLD = 0.5
ALREADY_RECOGNIZED = set()  # Track recognized faces

def send_alert_email(identity, location):
    """Send email alert with face detection info."""
    subject = "Alert: Recognized Person Detected"
    message = f"Person '{identity}' detected at {location} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient_email])
    print(f"Alert email sent for {identity} at {location}.")

def recognize_face(cropped_face):
    """Use DeepFace for face recognition."""
    try:
        result = DeepFace.find(img_path=cropped_face, db_path=photos_folder, enforce_detection=False)
        if result:
            identity = os.path.basename(result[0]['identity'].iloc[0])
            return identity
    except Exception as e:
        print(f"Face recognition error: {e}")
    return "Unknown"

def process_frame(frame):
    """Process each frame to detect faces and recognize them."""
    resized_frame = cv2.resize(frame, (640, 480))  # Resize for faster detection

    results = model.predict(resized_frame, conf=CONFIDENCE_THRESHOLD)
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get bounding box coordinates
            confidence = box.conf[0]  # Confidence score

            if confidence > CONFIDENCE_THRESHOLD:
                # Crop the detected face
                cropped_face = frame[y1:y2, x1:x2]

                # Recognize the face
                identity = recognize_face(cropped_face)
                location = f"CCTV at ({x1},{y1})"  # Simplified location info

                # Avoid duplicate recognition and send email alert
                if identity != "Unknown" and identity not in ALREADY_RECOGNIZED:
                    send_alert_email(identity, location)
                    ALREADY_RECOGNIZED.add(identity)  # Mark identity as recognized

                # Draw bounding box and identity label
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.putText(frame, identity, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    return frame

# Main loop for video stream processing
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Process each frame and display
    processed_frame = process_frame(frame)

    cv2.imshow("Face Detection and Recognition", processed_frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
