import cv2 as cv
import ctypes
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


def main():

    # load image and convert to gray
    img = cv.imread('image2.jpg', 1)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 5)

    # define circles
    rows = gray.shape[0]
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
                              param1=100, param2=30,
                              minRadius=5, maxRadius=60)

    # create empty list and start variables
    my_variable_array = []
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
            radius = i[2]

            # detect color of center and add them to array
            color = img[(center[1], center[0])]

            # printing and counting red
            if 80 > color[0] >= 0 and 80 > color[1] >= 0 and 255 >= color[2] > 130:
                farbe = "Rot"
                zr = zr+1
            else:
                # printing and counting yellow
                if 180 > color[0] >= 0 and 235 >= color[1] > 130 and 255 > color[2] > 125:
                    farbe = "Gelb"
                    zg = zg + 1
                else:
                    farbe = "Hintergrund"

            myvariable = (center[0], center[1], farbe)
            my_variable_array.append(myvariable)

            # draw circle center in pink
            # cv.circle(img, center, 1, (255, 0, 255), 2)

            # draw circle outline in pink
            radius = i[2]
            # cv.circle(img, center, radius, (255, 0, 255), 3)

        # sort array
        my_variable_array.sort(reverse=False)
        test = (split(my_variable_array, 6))

        # sort columns, one arrays for single column
        # colum1
        test[0].sort(key=lambda x: x[1])
        spalte1 = test[0]
        # column2
        test[1].sort(key=lambda x: x[1])
        spalte2 = test[1]
        # column3
        test[2].sort(key=lambda x: x[1])
        spalte3 = test[2]
        # column4
        test[3].sort(key=lambda x: x[1])
        spalte4 = test[3]
        # column5
        test[4].sort(key=lambda x: x[1])
        spalte5 = test[4]
        # column 6
        test[5].sort(key=lambda x: x[1])
        spalte6 = test[5]
        # column 7
        test[6].sort(key=lambda x: x[1])
        spalte7 = test[6]


        #where is a free spot
        #column 1
        print("Spalte 1:", spalte1)
        lastfree("1", spalte1, img, radius)
        # column 2
        print("Spalte 2:", spalte2)
        lastfree("2", spalte2, img, radius)
        # column 3
        print("Spalte 3:", spalte3)
        lastfree("3", spalte3, img, radius)
        # column 4
        print("Spalte 4:", spalte4)
        lastfree("4", spalte4, img, radius)
        # column 5
        print("Spalte 5:", spalte5)
        lastfree("5", spalte5, img, radius)
        # column 6
        print("Spalte 6:", spalte6)
        lastfree("6", spalte6, img, radius)
        # column 7
        print("Spalte 7:", spalte7)
        lastfree("7", spalte7, img, radius)

        # is there a winner
        winnery = False
        # vertical
        # column 1
        if winnery == False:
            winnery = vertwinner(spalte1, "1")
        # column 2
        if winnery == False:
            winnery = vertwinner(spalte2, "2")
        # column 3
        if winnery == False:
            winnery = vertwinner(spalte3, "3")
        # column 4
        if winnery == False:
            winnery = vertwinner(spalte4, "4")
        # column 5
        if winnery == False:
            winnery = vertwinner(spalte5, "5")
        # column 6
        if winnery == False:
            winnery = vertwinner(spalte6, "6")
        # column 7
        if winnery == False:
            winnery = vertwinner(spalte7, "7")

        # horizontal
        if winnery == False:
            winnery = horwinner(test)

        # diagonal


        # print results
        # print(my_variable_array)
        # print("Anzahl rote Steine:", zr)
        # print("Anzahl gelbe Steine:", zg)
        print("1",winnery)
        # winner?
        if winnery == False:
            # who is next if red started
            if start == "red":
                if zr > zg:
                    print("Gelb ist dran!")
                else:
                    print("Rot ist dran!")

            # who is next if yellow started
            if start == "yellow":
                if zg > zr:
                    print("Rot ist dran!")
                else:
                    print("Gelb ist dran!")


    # show image and detected circles
    cv.imshow("Vier Gewinnt", img)
    cv.waitKey(0)

    return 0


# last free function
def lastfree(z, spalte, img, radius):
    for myvariable in spalte:
        if myvariable[2] == "Hintergrund":
            last = myvariable
        else:
            print("Letzte freie Stelle in Spalte", z, ":", last)
            # draw circle center
            center = (last[0], last[1])
            cv.circle(img, center, 1, (0, 0, 0), 2)
            # draw circle outline
            cv.circle(img, center, radius, (0, 0, 0), 3)
            break
    return


# vertical winner function
def vertwinner(spalte, z):
    rot = 0
    gelb = 0
    winnery = False
    for myvariable in spalte:
        if myvariable[2] == "Rot":
            rot = rot + 1
            if rot == 4:
                print("Rot hat in Spalte", z, "gewonnen!")
                winnery = True
                return winnery
        else:
            rot = 0

    for myvariable in spalte:
        if myvariable[2] == "Gelb":
            gelb = gelb + 1
            if gelb == 4:
                print("Gelb hat in Spalte", z, "gewonnen!")
                winnery = True
                return winnery
        else:
            gelb = 0
    return winnery


# horizontal winner function
def horwinner(test):
    rot = 0
    gelb = 0
    winnery = False
    for y in range(0, 6):
        for x in range (0, 7):
            spalte = test[x]
            element = spalte[y]
            if element[2] == "Rot":
                rot = rot+1
                if rot == 4:
                    print("Rot hat in Zeile", x, "gewonnen")
                    winnery = True
                    return winnery
            else:
                rot = 0

    for y in range(0, ):
        for x in range (0, 7):
            spalte = test[x]
            element = spalte[y]
            if element[2] == "Gelb":
                gelb = gelb+1
                if rot == 4:
                    print("Gelb hat in Zeile", x, "gewonnen")
                    winnery = True
                    return winnery
            else:
                gelb = 0
    else:
        return winnery


# split array function
def split(arr, size):
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr = arr[size:]
    arrs.append(arr)
    return arrs


# main function
if __name__ == "__main__":
    main()
