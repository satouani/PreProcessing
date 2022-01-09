# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np 
import os, sys
import imutils
from imutils import face_utils
import cv2
import dlib 
from watermarking import transparentOverlay
import matplotlib
import shutil
from PIL import Image 

print("Current working directory: {0}".format(os.getcwd()))

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("D:\\python_code\\shape_predictor_68_face_landmarks.dat")
glass = cv2.imread("..\\Utilities\\glass5.png",cv2.IMREAD_UNCHANGED)
moustache = cv2.imread("..\\Utilities\\png_moustache2.png", cv2.IMREAD_UNCHANGED)
#moustache = cv2.imread("D:\python_code\Images\moustache.png", cv2.IMREAD_UNCHANGED)
img = cv2.imread("..\\Utilities\\monPro.jpg")




# loop over the frames from the video stream

# grayscale
frame = img
frame = imutils.resize(frame, height=550)
cv2.imwrite('D:\\3A\\projetS9\\preProcessing\\frame.jpg' ,frame)

'''
pathDi = "D:\\3A\\projetS9\\PreProcessing"
matplotlib.image.imsave("D:\\python_code\\Images\\imgToSaveV.jpg", frame)
os.rename(  "D:\\python_code\\Images\\imgToSaveV.jpg", "D:\\3A\\projetS9\\PreProcessing\\imgTosaveV.jpg")
os.replace( "D:\\python_code\\Images\\imgToSaveV.jpg", "D:\\3A\\projetS9\\PreProcessing\\imgTosaveV.jpg")
shutil.move("D:\\python_code\\Images\\imgToSaveV.jpg", "D:\\3A\\projetS9\\PreProcessing\\imgTosaveV.jpg")
'''

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 # detect faces in the grayayscale frame
rects = detector(gray, 0)

# loopop over found faces
for rect in rects:
    shape1 = predictor(frame, rect)
    shape = face_utils.shape_to_np(shape1)

    eyeLeftSide = 0
    eyeRightSide = 0
    eyeTopSide = 0
    eyeBottomSide = 0

    moustacheLeftSide = 0
    moustacheRightSide = 0
    moustacheTopSide = 0
    moustacheBottomSide = 0

    for (i, (x, y)) in enumerate(shape):
        if (i + 1) == 37:
            eyeLeftSide = x - 40
        if (i + 1) == 38:
            eyeTopSide = y - 30
        if (i + 1) == 46:
            eyeRightSide = x + 40
        if (i + 1) == 48:
            eyeBottomSide = y + 30
        
        if (i + 1) == 2:
            moustacheLeftSide = x
            moustacheTopSide = y - 10
        if (i + 1) == 16:
            moustacheRightSide = x
        if (i + 1) == 9:
            moustacheBottomSide = y

    eyesWidth= abs(eyeRightSide - eyeLeftSide)


    # add glasses
    fitedGlass = imutils.resize(glass, width=eyesWidth)
    cv2.imwrite("D:\\3A\\projetS9\\PreProcessing\\glass.png" ,fitedGlass)
    frame = transparentOverlay(frame, fitedGlass, x= eyeLeftSide, y= eyeTopSide)

    moustacheWidth= abs(moustacheRightSide - moustacheLeftSide)
    # add moustache
    fitedMoustache = imutils.resize(moustache, width=moustacheWidth)
    cv2.imwrite("D:\\3A\\projetS9\\PreProcessing\\fitedMoustache1.png" ,fitedMoustache)
    frame = transparentOverlay(frame, fitedMoustache, x= moustacheLeftSide, y= moustacheTopSide, scale=1)
    cv2.imshow("fited", fitedMoustache)
    cv2.imshow("face", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

