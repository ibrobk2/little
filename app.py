import cv2 as cv


cap = cv.VideoCapture(0)

while True:
    ret, image = cap.read()
    
    cv.imshow("VIDEO CAPTURED", image)
    
    key = cv.waitKey(1)
    
    if key==ord('q'):
        cap.release()
        cv.destroyAllWindows()