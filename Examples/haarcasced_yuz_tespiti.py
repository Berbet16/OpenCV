import cv2
import numpy as np

#resmi okuttuk
img= cv2.imread('kalabalik2.jpg')

#yüz tanımada kullanılacak algoritma
yuz_casc=cv2.CascadeClassifier('onyuz.xml')

griton=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
yuzler=yuz_casc.detectMultiScale(griton,1.1,4)

#yüzleri çağıralım ve kare içerisinde göstermek için kullanılır.
for(x,y,w,h) in yuzler:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow('yuzler',img) # çerçeve ismi 
cv2.waitKey(0) #herhandi tuşa bastığımızda kapansın.
cv2.destroyAllWindows() #işlemi tamamlama