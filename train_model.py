import cv2
import numpy as np
from PIL import Image
import os
class All:
    path = 'D:\OOP project\OOP Project ATM\Dataset'

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    

    # function to get the images and label data
    def getImagesAndLabels(path):
        detector = cv2.CascadeClassifier("D:\OOP project\OOP Project ATM\haarcascade_frontalface_default.xml")
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
        faceSamples=[]
        ids = []

        for imagePath in imagePaths:

            PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
            img_numpy = np.array(PIL_img,'uint8')

            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)

            for (x,y,w,h) in faces:
                faceSamples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)

        return faceSamples,ids

    print ("\n Training faces. It will take a few seconds. Wait ...")
    faces,ids = getImagesAndLabels(path)
    recognizer.train(faces, np.array(ids))

    recognizer.write('D:\OOP project\OOP Project ATM\ training.yml') 

    # Print the numer of faces trained and end program
    print("\n {0} faces trained. Exiting Program".format(len(np.unique(ids))))