
import cv2
import numpy as np
import face_recognition

imgReference = face_recognition.load_image_file('Images_Attendance/person_one.jpg')
imgReference = cv2.cvtColor(imgReference, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('Images_Attendance/person_two.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceloc = face_recognition.face_locations(imgReference)[0]
encodeReference = face_recognition.face_encodings(imgReference)[0]
cv2.rectangle(imgReference, (faceloc[3], faceloc[0]), (faceloc[1], faceloc[2]), (155, 0, 255), 2)

facelocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[1]
cv2.rectangle(imgTest, (facelocTest[3], facelocTest[0]), (facelocTest[1], facelocTest[2]), (155, 0, 255), 2)

results = face_recognition.compare_faces([encodeReference], encodeTest)
faceDis = face_recognition.face_distance([encodeReference], encodeTest)
print(results, faceDis)
cv2.putText(imgTest, f'{results} {round(faceDis[0],2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)

cv2.imshow('reference', imgReference)
cv2.imshow('test', imgTest)
cv2.waitKey(0)
