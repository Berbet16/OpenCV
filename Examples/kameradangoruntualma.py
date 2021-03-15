
import cv2

#kamera bağlantısı için kullanılır
kamera = cv2.VideoCapture(0)

while True:
    ret, goruntu = kamera.read()
    griton = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('Görüntü', goruntu)
    cv2.imshow('Gri Ton', griton)
    
    if cv2.waitKey(25) & 0xFF == ord('x'):
        break

kamera.release()
cv2.destroyAllWindows()
    