import cv2 as cv
import numpy as np


# main function
def main():

    # create empty list and initial variables
    my_variable_array = []
    start = "red"
    zr = 0
    zg = 0
    winnery = False

    # load image and convert to gray
    img = cv.imread('Test.jpg', 1)
    img = cv.resize(img, (0, 0), fx=0.5, fy=0.5)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 5)

    # detect circles
    rows = gray.shape[0]
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
                              param1=100, param2=20,
                              minRadius=1, maxRadius=40)

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
                zr = zr + 1
            else:
                # printing and counting yellow
                if 180 > color[0] >= 0 and 235 >= color[1] > 130 and 255 > color[2] > 125:
                    farbe = "Gelb"
                    zg = zg + 1
                else:
                    farbe = "Hintergrund"

            # create variables for circles and add to array
            myvariable = (center[0], center[1], farbe)
            my_variable_array.append(myvariable)

            # draw circle center and outline in pink
            # cv.circle(img, center, 1, (255, 0, 255), 2)
            # radius = i[2]
            # cv.circle(img, center, radius, (255, 0, 255), 3)

        # sort game board
        test = sortboard(my_variable_array)

        # detect game situation - is there a winner?
        if winnery == False:
            winnery = vertwinner(test, img, radius)
        if winnery == False:
            winnery = horwinner(test, img, radius)
        # diagonal winner
        # ???

        # who is next?
        if winnery == False:
            next(start, zr, zg)

            # where is a free spot
            lastfree(test, img, radius)

    # show image and detected circles
    cv.imshow("Vier Gewinnt", img)
    cv.waitKey(0)

    return 0


# sort game board correctly
def sortboard (my_variable_array):
    my_variable_array.sort(reverse=False)
    test = (split(my_variable_array, 6))
    for y in range(0, 7):
        test[y].sort(key=lambda x: x[1])
    return test


# vertical winner function
def vertwinner(test, img, radius):
    rot = 0
    gelb = 0
    winnery = False
    centerlist = []
    for x in range(0, 7):
        spalte = test[x]

        for myvariable in spalte:
            if myvariable[2] == "Rot":
                rot = rot + 1
                centerlist.append(myvariable)
                if rot == 4:
                    print("Rot hat in Spalte", x+1, "von Links gewonnen!")
                    winnery = True
                    # mark winning pieces
                    for myvariable in centerlist:
                        center = (myvariable[0], myvariable[1])
                        #cv.circle(img, center, 1, (255, 255, 255), 2)
                        cv.circle(img, center, radius, (255, 255, 255), 3)
                    return winnery
            else:
                rot = 0
                centerlist = []

        for myvariable in spalte:
            if myvariable[2] == "Gelb":
                gelb = gelb + 1
                centerlist.append(myvariable)
                if gelb == 4:
                    print("Gelb hat in Spalte", x+1, "von Links gewonnen!")
                    winnery = True
                    # mark winning pieces
                    for myvariable in centerlist:
                        center = (myvariable[0], myvariable[1])
                        #cv.circle(img, center, 1, (255, 255, 255), 2)
                        cv.circle(img, center, radius, (255, 255, 255), 3)
                    return winnery
            else:
                gelb = 0
                centerlist = []
    return winnery


# horizontal winner function
def horwinner(test, img, radius):
    winnery = False
    for y in range(0, 5):
        rot = 0
        centerlist = []
        for x in range(0, 6):
            spalte = test[x]
            element = spalte[y]
            if element[2] == "Rot":
                rot = rot+1
                centerlist.append(element)
                if rot == 4:
                    print("Rot hat in Reihe", y+1,"von oben gewonnen!")
                    winnery = True
                    for element in centerlist:
                        center = (element[0], element[1])
                        #cv.circle(img, center, 1, (255, 255, 255), 2)
                        cv.circle(img, center, radius, (255, 255, 255), 3)
                    return winnery
            else:
                rot = 0
                centerlist = []

    for y in range(0, 6):
        gelb = 0
        centerlist = []
        for x in range(0, 6):
            spalte = test[x]
            element = spalte[y]
            if element[2] == "Gelb":
                gelb = gelb+1
                centerlist.append(element)
                if gelb == 4:
                    print("Gelb hat in Reihe", y+1,"von oben gewonnen!")
                    winnery = True
                    for element in centerlist:
                        center = (element[0], element[1])
                        #cv.circle(img, center, 1, (255, 255, 255), 2)
                        cv.circle(img, center, radius, (255, 255, 255), 3)
                    return winnery
            else:
                gelb = 0
                centerlist = []
    else:
        return winnery
    return


# who is next function
def next(start, zr, zg):
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
    return


# last free spot function
def lastfree(test, img, radius):
    for x in range(0, 7):
        spalte = test[x]
        # print("Spalte", x, ":", spalte)
        for myvariable in spalte:

            if myvariable[2] == "Hintergrund":
                last = myvariable
            else:
                # print("Letzte freie Stelle in Spalte", x, ":", last)
                # draw circle center
                center = (last[0], last[1])
                cv.circle(img, center, 1, (0, 0, 0), 2)
                # draw circle outline
                cv.circle(img, center, radius, (0, 0, 0), 3)
                break
    return


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

