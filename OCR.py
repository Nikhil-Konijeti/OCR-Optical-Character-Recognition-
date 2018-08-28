#importing libraries
from PIL import Image
import pytesseract
import cv2
import os
import nltk 
#nltk.download('words')
import string
from pdf2image import convert_from_path
    
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

'''
pages = convert_from_path('Gift_Deed.pdf',500) 
for page in pages:
    file = "{}.jpg".format(count)
    print(file)
    count += 1
    page.save(file,'JPEG')
'''

count = 11  
for i in range(1,count+1):
    im = cv2.imread(str(i)+".jpg")
    x = preprocess(im,i)
    print(i)
    with open('out.txt','a') as f:
        f.write(ocr(x).encode('ascii', 'ignore'))
        
        
english_words = set(w.lower() for w in nltk.corpus.words.words())

key=[]
        
# Remove punctuation marks
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
    if len(eng)<4:
        continue
    nf.write('\n')
out.close()
nf.close()