import cv2
import time
import oneM2Mget 
from Speak import text_to_speech
from getLUX import calculate_luminance
from onem2mpost import create_cin
# from faceDistance import getDistance

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Constants for distance calculation
KNOWN_FACE_WIDTH = 16.5  # Assume the average face width in centimeters (e.g., 16.5 cm)
FOCAL_LENGTH = 500.0  # Assume the focal length of the camera (e.g., 500 pixels)

def count_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return len(faces)

def calculate_distance(face_width_pixels):
    return (KNOWN_FACE_WIDTH * FOCAL_LENGTH) / face_width_pixels

def take_photo_and_count_faces():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Failed to open camera.")
        return

    prev_num_faces = 0  # Previous number of faces
    speech_played = False
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break
        
        num_faces = count_faces(frame)
        print(f"Previous number of faces: {prev_num_faces}, Current number of faces: {num_faces}")
        luminnce = calculate_luminance(frame)
        url = f"http://dev-onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-L001-03/Data"
        create_cin(url,[luminnce,num_faces])
        if prev_num_faces != num_faces:
            for (x, y, w, h) in face_cascade.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)):
                face_width_pixels = w
                distance = calculate_distance(face_width_pixels)
                print(f"Distance to face: {distance} cm")
                if distance is not None and distance < 40:   # Check if distance is valid (not None) and less than 40
                    if not speech_played:                    # Check if speech has already been played for this detection
                        try:
                            print("hianshi")
                            response_data = oneM2Mget.getTemperature()
                            con_value = response_data
                            data = f"Welcome to Smart City Living Lab. The current value of CO2 is {con_value[1]}, temperature is {con_value[2]}, and humidity is {con_value[3]}."
                            text_to_speech(data)
                            # print(response_data)
                            speech_played = True             # Set the flag to True to indicate that speech has been played
                        except Exception as e:
                            print(f"Error: {e}")
                    else:
                        speech_played = False

            cv2.imshow('Frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        prev_num_faces = num_faces  # Update previous number of faces

        time.sleep(3)  # Wait for 3 seconds before capturing the next photo

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    take_photo_and_count_faces()