import cv2

cv2. destroyAllWindows()

imagen = cv2.imread("/home/pc/Documentos/Data PDI/MINIMERCADO/ARROZ DIANA/47086962-087c-417a-a8a7-7ad559b78e9e.jpg")
imagen_gris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
imagen_sin = cv2.GaussianBlur(imagen_gris,(5,5),cv2.BORDER_DEFAULT)
imagen_bin = cv2.threshold(imagen_sin, 127, 255, cv2.THRESH_BINARY)[1]
contours,_ = cv2.findContours(imagen_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    area = cv2.contourArea(c)
    if area > 1000:
        cv2.drawContours(imagen, [c], 0, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imshow("original",imagen)
cv2.imshow('Imagen Gris',imagen_gris)
cv2.imshow('Imagen sin ruido',imagen_sin)
cv2.imshow('Binarizado',imagen_bin)
cv2.waitKey()