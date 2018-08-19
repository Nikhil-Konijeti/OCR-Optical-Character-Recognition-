#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 21:06:25 2018

@author: nikhilkonijeti
"""


#importing libraries
from PIL import Image
import pytesseract
import cv2
import os
import textract
from pdf2image import convert_from_path


def  preprocess (image):
    
    try:
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    except:
        gray = image

    filename = "{}.jpg".format(os.getpid())
    cv2.imwrite(filename, gray)

    return filename


def  ocr(filename):
    path = os.getcwd()
    im = Image.open(path+"/"+filename)
    text = pytesseract.image_to_string(im)
    print(text)
    os.remove(filename)
    

pages  =  convert_from_path('Rent agreement 2017.pdf',500)
count=1
for page in pages:
    file = "{}.jpg".format(count)
    print(file)
    count+=1
    page.save(file,'JPEG')
    
    
for i in range(1,count+1):
    im = cv2.imread(str(i)+".jpg")
    x = preprocess(im)
    print(ocr(x))
    
    