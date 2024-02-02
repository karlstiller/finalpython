import zipfile

from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

# the rest is up to you!
with zipfile.ZipFile('readonly/small_img.zip') as zip:
    zipList = zip.infolist()
    for info in zipList:
        with zip.open(info) as picFile:
            print(picFile)
        print(info.filename)
