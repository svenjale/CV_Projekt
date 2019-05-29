import cv2 as cv
import sys
import numpy as np


# connection to webcam
# cam= cv2.VideoCapture(0)
# while(True):
#    ret, video = cam.read()
#    video = cv2.flip(video,1)
#    cv2.imshow('Video', video)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break
# cam.release()
# cv2.destroyAllWindows()


def main(argv):
    default_file = 'images.jpg'
    filename = argv[0] if len(argv) > 0 else default_file

    # load image and convert to gray
    img = cv.imread('image.jpg', 1)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 5)

    # define circles
    rows = gray.shape[0]
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
                              param1=100, param2=30,
                              minRadius=5, maxRadius=60)

    my_list = []

    # draw circles and center
    if circles is not None:
        circles = np.uint16(np.around(circles))
        z = 0
        for i in circles[0, :]:
            z=z+1
            center = (i[0], i[1])
            # draw circle center
            cv.circle(img, center, 1, (255, 0, 255), 2)
            #print(center)

            # draw circle outline
            radius = i[2]
            cv.circle(img, center, radius, (255, 0, 255), 3)
            my_list.append(center)

        print("Anzahl an Kreisen:")
        print(z)
        print("Koordinaten der Kreismittelpunkte:")
        print(my_list)


    # show image and detected circles
    cv.imshow("Erkannte Kreise", img)
    cv.waitKey(0)

    return 0


# wtf?!
if __name__ == "__main__":
    main(sys.argv[1:])


#load image
#img = cv2.imread('Testbild.jpg', 1)
#cv2.imshow('Image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()