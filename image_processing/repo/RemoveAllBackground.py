#******************************************************************
#CLass created to pdi
#******************************************************************

import cv2

from image_processing.repo.ImageData import ImageData


class RemoveAllBackground:

    def __init__(self):
        print('start')

    def startProccesWith(self, imageList):
        for imageItem in imageList:
            # Leer la imagen

            img = cv2.imread(imageItem.image)

            # convert to gray
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # threshold grayscale image to extract glare
            mask = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)[1]

            # use mask with input to do inpainting
            result = cv2.inpaint(img, mask, 21, cv2.INPAINT_TELEA)
            libre_ruido = cv2.GaussianBlur(result, (5, 5), cv2.BORDER_DEFAULT)

            cv2.imshow("IMAGE", img)
            cv2.imshow("QUITAR FLASH", libre_ruido)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            img.setImage.setResultImage(libre_ruido)

path=""
name = ""
label = ""
image = "/home/pc/Documentos/Final PDI/view/test.jpg"

img=ImageData(path,name,label,image)
##RemoveAllBackground().startProccesWith([img])
