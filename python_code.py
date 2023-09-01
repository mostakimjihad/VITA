import face_recognition
import cv2
import numpy as np
import csv
import os
import glob
from datetime import datetime
import pyttsx3
import serial
import time

commander = serial.Serial('/dev/ttyACM0', 9600)
speaker = pyttsx3.init()
speaker.setProperty('rate', 130)
video_capture = cv2.VideoCapture(0)

jihad_image = face_recognition.load_image_file("photos/jihad.jpg")
jihad_encoding = face_recognition.face_encodings(jihad_image)[0]

kabbo_image = face_recognition.load_image_file("photos/kabbo.jpg")
kabbo_encoding = face_recognition.face_encodings(kabbo_image)[0]

noor_image = face_recognition.load_image_file("photos/noor.jpg")
noor_encoding = face_recognition.face_encodings(noor_image)[0]

rodshi_image = face_recognition.load_image_file("photos/rodshi.jpg")
rodshi_encoding = face_recognition.face_encodings(rodshi_image)[0]

shojib_image = face_recognition.load_image_file("photos/shojib.jpg")
shojib_encoding = face_recognition.face_encodings(shojib_image)[0]

ahmed_image = face_recognition.load_image_file("photos/ahmed.jpg")
ahmed_encoding = face_recognition.face_encodings(ahmed_image)[0]


known_face_encoding = [jihad_encoding, rodshi_encoding, noor_encoding, kabbo_encoding, ahmed_encoding, shojib_encoding]
known_face_names = ["jihad", "rodshi", "noor", "kabbo", "ahmed", "shojib"]

students = known_face_names.copy()

face_locations = []
face_encodings = []
face_names = []

s = True

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(current_date + '.csv', 'w+', newline='' )
lnwriter = csv.writer(f)

while True:
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame,(0,0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:,:,::-1]
    
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
            best_match_index = np.argmin(face_distance)
            
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)
            if name in known_face_names:
                if name in students:
                    
                    if name == "jihad":
                        speaker.say("hey, mostakim jihad")
                        speaker.runAndWait()
                        commander.write(b'h')
                        time.sleep(2)
                        speaker.say("I am vita")
                        speaker.runAndWait()
                        speaker.say("virtual teacher assistant that you have made")
                        speaker.runAndWait()
                        speaker.say("Thanks for creating me")
                        speaker.runAndWait()
                        time.sleep(1)
                        speaker.say("let me show you. what can i do")
                        speaker.runAndWait()
                        speaker.say("I can give hi to people")
                        speaker.runAndWait()
                        commander.write(b'h')
                        speaker.say("like this")
                        speaker.runAndWait()
                        time.sleep(2)
                        speaker.say("I can give salam")
                        speaker.runAndWait()
                        commander.write(b's')
                        speaker.say("like this")
                        speaker.runAndWait()
                        time.sleep(2)
                        speaker.say("I can turn around")
                        speaker.runAndWait()
                        commander.write(b'b')
                        speaker.say("like this")
                        speaker.runAndWait()
                        time.sleep(2)
                        speaker.say("your attendance has been marked")
                        speaker.runAndWait()
                        speaker.say("Have a good day")
                        speaker.runAndWait()

                    if name == "kabbo":
                        speaker.say("hey, Rahat khondokar Kabbo")
                        speaker.runAndWait()
                        commander.write(b'h')
                        time.sleep(2)
                        speaker.say("your attendance has been marked")
                        speaker.runAndWait()
                        speaker.say("Is there any student left")
                        speaker.runAndWait()
                        commander.write(b'b')
                        time.sleep(2)
                        speaker.say("one more thing")
                        speaker.runAndWait()
                        speaker.say("Be attentive in your class")
                        speaker.runAndWait()
                    if name == "rodshi":
                        speaker.say("Assalamu alaikum, mam")
                        speaker.runAndWait()
                        commander.write(b's')
                        time.sleep(2)
                        speaker.say("I am your personal assistant")
                        speaker.runAndWait()
                        speaker.say("vita")
                        speaker.runAndWait()
                        speaker.say("Mam you are taking Artificial Intelligence")
                        speaker.runAndWait()
                        speaker.say("And this is D2 section")
                        speaker.runAndWait()
                        time.sleep(1)
                        for a in students:
                            if a == "rodshi":
                                continue
                            speaker.say(a)
                            speaker.runAndWait()
                        speaker.say("are absent today")
                        speaker.runAndWait()

                    if name == "noor":
                        speaker.say("hey, Taj noor fahim")
                        speaker.runAndWait()
                        commander.write(b'h')
                        time.sleep(2)
                        speaker.say("your attendance has been marked")
                        speaker.runAndWait()
                        speaker.say("Is there any student left")
                        speaker.runAndWait()
                        commander.write(b'b')
                        time.sleep(2)
                    
                    if name == "ahmed":
                        speaker.say("hey, ahmed islam")
                        speaker.runAndWait()
                        commander.write(b'h')
                        time.sleep(2)
                        speaker.say("your attendance has been marked")
                        speaker.runAndWait()
                        speaker.say("Is there any student left")
                        speaker.runAndWait()
                        commander.write(b'b')
                        time.sleep(2)
                    
                    if name == "shojib":
                        speaker.say("hey, asmaul hassan shojib")
                        speaker.runAndWait()
                        commander.write(b'h')
                        time.sleep(2)
                        speaker.say("your attendance has been marked")
                        speaker.runAndWait()
                        speaker.say("Is there any student left")
                        speaker.runAndWait()
                        commander.write(b'b')
                        time.sleep(2)

                    students.remove(name)
                    print(students)
                    current_date = now.strftime("%H-%M-%S")
                    lnwriter.writerow([name, current_date])
    cv2.imshow("attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
f.close()
