#
#
# import numpy as np
# import cv2
#
# img = cv2.imread("../src/assets/img/2013-02-26_15_19_36.jpg")
# pts = np.array([[433,364],[318,452],[339,550],[382,529]])
#
# ## (1) Crop the bounding rect
# rect = cv2.boundingRect(pts)
# x,y,w,h = rect
# croped = img[y:y+h, x:x+w].copy()
#
# ## (2) make mask
# pts = pts - pts.min(axis=0)
#
# mask = np.zeros(croped.shape[:2], np.uint8)
# cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)
#
# ## (3) do bit-op
# dst = cv2.bitwise_and(croped, croped, mask=mask)
#
# ## (4) add the white background
# bg = np.ones_like(croped, np.uint8)*255
# cv2.bitwise_not(bg,bg, mask=mask)
# dst2 = bg+ dst
#
#
# cv2.imwrite("croped.png", croped)
# cv2.imwrite("mask.png", mask)
# cv2.imwrite("dst.png", dst)
# cv2.imwrite("dst2.png", dst2)

def getTheSpots(camera, frame):
    import numpy as np
    import cv2
    from .helper import ObjectCreator

    # Variaveis
    mapImgs = []

    # Resize a image para o tamanho do canvas
    img = cv2.resize(frame, (720, 406))

    for (i, item) in enumerate(camera.spots):
        cordinates = []
        for cord in item.cords:
            cordinates.append([cord.x, cord.y])
        pts = np.array(cordinates)
        rect = cv2.boundingRect(pts)
        x, y, w, h = rect

        croped = img[y:y + h, x:x + w].copy()

        pts = pts - pts.min(axis=0)
        mask = np.zeros(croped.shape[:2], np.uint8)

        cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)
        dst = cv2.bitwise_and(croped, croped, mask=mask)


        objeto = ObjectCreator()
        objeto.id = item.id
        objeto.image = dst

        mapImgs.append(objeto)

        # bg = np.ones_like(croped, np.uint8) * 255
        # cv2.bitwise_not(bg, bg, mask=mask)
        # dst2 = bg + dst
        # cv2.imwrite("./images-cut/0"+str(i)+".png", croped)
        #cv2.imwrite("../src/assets/croped/mask"+str(i)+".png", mask)
        # cv2.imwrite("./images-cut/1"+str(i)+".png", dst)
        # cv2.imwrite("./images-cut/2"+str(i)+".png", dst2)

    return mapImgs