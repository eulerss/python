#Tomado de: https://realpython.com/face-recognition-with-python/
import cv2
import sys

# Create the haar cascade
faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

# Read the image
image = cv2.imread('./grupo3.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
# Modificar los valores acorde a la imagen
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=3,
    minSize=(10, 10),
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

#cv2.imshow("Faces found", image)
cv2.imwrite('./faces_detected_grupo3.jpg',image)
