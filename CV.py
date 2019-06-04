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

    # create empty list and start variables
    my_list = []
    my_colors =[]
    start = "red"
    zr = 0
    zg = 0

    # draw circles and center
    if circles is not None:
        circles = np.uint16(np.around(circles))
        z = 0
        for i in circles[0, :]:
            z=z+1
            center = (i[0], i[1])

            # detect color of center and add them to array
            color = img[(center[1], center[0])]

            # printing and counting red
            if 61 > color[0] > 39 and 61 > color[1] > 39 and 251 > color[2] > 239:
                my_colors.append("rot")
                zr = zr+1
            else:
                # printing and counting yellow
                if 99 > color[0] > 85 and 230 > color[1] > 220 and 245 > color[2] > 235:
                    my_colors.append("gelb")
                    zg = zg + 1
                else:
                    my_colors.append("blau")

            # draw circle center and add to array
            cv.circle(img, center, 1, (255, 0, 255), 2)
            my_list.append(center)

            # draw circle outline
            radius = i[2]
            cv.circle(img, center, radius, (255, 0, 255), 3)

        # print results
        print("Farben:", my_colors)
        print("Anzahl an Kreisen:", z)
        print("Koordinaten der Kreismittelpunkte:", my_list)
        print("Anzahl rote Steine:", zr)
        print("Anzahl gelbe Steine:", zg)

        # who is next if red started
        if start == "red":
            if zr>=zg:
                print("Rot ist dran!")
            else:
                print("Gelb ist dran!")

        # who is next if yellow started
        if start == "yellow":
            if zg >= zr:
                print("Gelb ist dran!")
            else:
                print("Rot ist dran!")

    # show image and detected circles
    cv.imshow("Erkannte Kreise", img)
    cv.waitKey(0)

    return 0


# wtf?!
if __name__ == "__main__":
    main(sys.argv[1:])
