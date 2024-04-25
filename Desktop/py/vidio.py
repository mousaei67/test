import cv2
import datetime

cap = cv2.VideoCapture("img/vtest.avi")

while(True):
 #while(cap.isOpened()):
    ret, frame = cap.read()
    i=0
    print(ret)
    if ret == True:
        # text = "Width: " + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        text = str(datetime.datetime.now().today())
        font = cv2.FONT_HERSHEY_SIMPLEX
        frame = cv2.putText(frame, text, (50, 50), font, 1, (0, 0, 0), 2)

        cv2.imshow('mousaei', frame)

        if cv2.waitKey(1000)  == ord('q'):
            break
    elif ret==False :
        
        break

cap.release()
cv2.destroyAllWindows()