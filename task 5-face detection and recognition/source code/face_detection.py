import cv2

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml'
)

# Load image
img = cv2.imread('face.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw rectangle around faces
for (x, y, w, h) in faces:
    cv2.rectangle(
        img,
        (x, y),
        (x+w, y+h),
        (255, 0, 0),
        2
    )

# Display output
cv2.imshow('Face Detection', img)

cv2.waitKey(0)
cv2.destroyAllWindows()