import cv2
from random import randrange


#Load data to train the bot
trained_face_data = cv2.CascadeClassifier('frontal_face.xml')

#chose an img to detect faces in
img = cv2.imread('rdj.png')

#Test multiple faces
#img = cv2.imread('test_multiple.jpeg')

)
#Capture Video from Webcam
"""try:
    webcam = cv2.VideoCapture(0)
except:
    print("aqui")

#Forever Loop for the frames
print("Frames")
while True:
    try:
    ####Read the current frame
        success_frame_read, read = webcam.read()

        #Convert the image to grayscale
        gray_scale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow("First ML Proyect", gray_scale_img)
        cv2.waitKey(1)
    except:
        print("Fallo")
        break
       """ 
  
gray_scale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Detect Faces cordinates
face_coordinates = trained_face_data.detectMultiScale(gray_scale_img)
#(x, y, w, h) = face_coordinates[0]
#Draw a rectangle
for (x, y, w, h) in face_coordinates[:]:
    cv2.rectangle(img, (x, y), (x + w, y + h), (randrange(256), randrange(256), 
                                                randrange(256)), 2)

cv2.imshow("First ML Proyect", img)
cv2.waitKey()