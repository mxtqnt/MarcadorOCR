import cv2
import os
import easyocr
import pyautogui
import PIL
import numpy
from unidecode import unidecode
from parametros import PROCURADOS
from collections import Counter

procurados = []
encontrados = []

for item in PROCURADOS:
    procurados.append(unidecode(item))

img = pyautogui.screenshot(region=(24, 165, 412, 840))

pil_image = img.convert('RGB')
image = numpy.array(pil_image)

reader = easyocr.Reader(['pt'])
result = reader.readtext(image, detail='False', paragraph =True)


for res in result:
    top_left = tuple(res[0][0]) 
    bottom_right = tuple(res[0][2])

    if unidecode(res[1].upper()) in procurados:
        # print(unidecode(res[1].upper()))
        encontrados.append(unidecode(res[1].upper()))
        cv2.rectangle(image, top_left, bottom_right, (255, 0, 255), 2) 
    else:
        cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), 2) 
        cv2.putText(image, res[1], (top_left[0], top_left[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        
naoencontrados = [elemento for elemento in procurados if elemento not in encontrados]

print("Encontrados")
for item in encontrados:
    print(item)

print("\nNão encontrados")
for item in naoencontrados:
    print("'" + str(item) + "',")

cv2.imshow('Visao', image)
cv2.waitKey(0)  
    