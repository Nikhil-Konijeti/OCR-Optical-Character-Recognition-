#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 20:57:28 2018

@author: nikhilkonijeti
"""
from PIL import Image
import pytesseract
import cv2
import os
import nltk 
nltk.download('punkt')
nltk.download('popular')
dler = nltk.downloader.Downloader()
import string
from pdf2image import convert_from_path

import tkinter as tk
from tkinter import filedialog,Label,Button
import tkinter.messagebox

root=tk.Tk()
root.title('OCR')
answer=tkinter.messagebox.askquestion('Question 1','Would you like to input a PDF file')
if answer=='yes':
    filename1 = filedialog.askopenfilename(filetypes = (("PDF files","*.pdf"),("all files","*.*")))
    def  preprocess (image,i): 
        try:
            gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        except:
            gray = image
        filename = "{}.jpg".format(i*100)
        cv2.imwrite(filename, gray)
        return filename
        
    def ocr(filename):
        path = os.getcwd()
        im = Image.open(path+"/"+filename)
        text = pytesseract.image_to_string(im)
        os.remove(filename)
        return text
    
    count = 0
    pages = convert_from_path(filename1,500) 
    for page in pages:
        file = "{}.jpg".format(count)
        print(file)
        count += 1
        page.save(file,'JPEG')
        
    for i in range(0,count):
        im = cv2.imread(str(i)+".jpg")
        x = preprocess(im,i)
        print(i)
        with open('out.txt','a') as f:
            f.write(ocr(x).encode('ascii', 'ignore'))
            
    english_words = set(w.lower() for w in nltk.corpus.words.words())
                
    key=[]
                
    # Remove punctuation marks
    nf=open('new.txt', 'w').close()
    exclude = set(string.punctuation)
    out = open('out.txt','r')
    nf = open('new.txt','a')
    for line in out.readlines():
        for word in line.split():
            punc_free = " ".join([a for a in word.split() if a.lower() not in exclude])
            eng = " ".join([str(a)+" " for a in word.split() if a.lower() in english_words])
        key.append(eng)    
        for words in key:
            if len(words) == 1:
                key.remove(words)
        nf.write(eng)
    out.close()
    nf.close()  
    nf1 = open('new.txt','r')
    for line1 in nf1.readlines():
        def printText():
            label = Label(root, text= line1)
            label.pack() 
    root1 = tk.Tk()        
    button = Button(root1, text="Print Me", command=printText) 
    button.pack()
    root1.mainloop()
