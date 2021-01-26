import cv2




#Load data to train the bot
trained_face_data = cv2.CascadeClassifier('frontal_face.xml')

#chose an img to detect faces in
img = cv2.imread('rdj.png')

#Convert the image to grayscale
gray_scale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detect Faces
face_coordinates = trained_face_data.detectMultiScale(gray_scale_img)

print(face_coordinates)
cv2.imshow("First ML Proyect", gray_scale_img)
cv2.waitKey()

