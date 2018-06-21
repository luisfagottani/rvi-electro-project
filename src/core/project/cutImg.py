import numpy as np
import cv2
import json
import os



file = open("/Users/luis.agottani/Library/Application Support/rviapp/config.json", "r")
data = json.loads(file.read())

img = cv2.imread("./images/images.png")
img = cv2.resize(img, (720, 406))
for (i, item) in enumerate(data['camera01']['spots']):
    cordinates = []
    for cord in item['cords']:
        cordinates.append([cord['x'], cord['y']])
    pts = np.array(cordinates)
    rect = cv2.boundingRect(pts)
    x, y, w, h = rect
    croped = img[y:y + h, x:x + w].copy()
    pts = pts - pts.min(axis=0)

    ## GET ANGULE
    angle = cv2.minAreaRect(pts)[-1]
    n_width, n_height  = cv2.minAreaRect(pts)[1]
    center = cv2.minAreaRect(pts)[0]
    print(cv2.minAreaRect(pts))
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    # rotate the image to deskew it
    center = (n_width / 2, n_height / 2)
    M = cv2.getRotationMatrix2D(center, -18, 1.0)
    # cv2.imshow("teste", croped)
    # rotate = cv2.warpAffine(croped, M, (n_width, n_height))


    mask = np.zeros(croped.shape[:2], np.uint8)

    cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)
    rotate = cv2.warpAffine(croped, M, (int(n_width), int(n_height)))
    rotate2 = cv2.warpAffine(mask, M, (int(n_width), int(n_height)))
    dst = cv2.bitwise_and(rotate, rotate, mask=rotate2)

    cv2.imshow("teste", dst)
    cv2.waitKey(0)
    break;





    bg = np.ones_like(croped, np.uint8) * 255
    cv2.bitwise_not(bg, bg, mask=mask)
    dst2 = bg + dst
    cv2.imwrite("./images-cut/0"+str(i)+".png", croped)
    #cv2.imwrite("../src/assets/croped/mask"+str(i)+".png", mask)
    cv2.imwrite("./images-cut/1"+str(i)+".png", dst)
    cv2.imwrite("./images-cut/2"+str(i)+".png", dst2)