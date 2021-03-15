
import cv2

kamera= cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
kayit=cv2.VideoWriter('kayit.avi',fourcc,20.0,(640,480))

while(kamera.isOpened()):
    ret, video=kamera.read()
    if ret ==True:
        kayit.write(video)
        cv2.imshow('kayit',video)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
    else:
        break
kamera.release()
kayit.release()
cv2.destroyAllWindows()