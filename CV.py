import cv2

#connection to webcam
#cam= cv2.VideoCapture(0)
#while(True):
#    ret, video = cam.read()
#    video = cv2.flip(video,1)
#    cv2.imshow('Video', video)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break
#cam.release()
#cv2.destroyAllWindows()

#load image
img = cv2.imread('Testbild.jpg', 1)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()