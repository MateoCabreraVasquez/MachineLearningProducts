
import cv2

import PIL
from PIL import Image,ImageTk
from tkinter import *

from matplotlib import pyplot as pt
from matplotlib.image import imread
from control.control import Control

control=Control()


def takePicture():
    global setImage
    setImage=True

def addRectangles (locations):
    _, axe = pt.subplots()
    img=imread("hola.jpg")
    cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
    axe.imshow(cv2image)
    alto, ancho, _ = img.shape

    for item in locations:
        axe.add_patch(item)
    pt.savefig('result.png')




width, height = 800, 700

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

root = Tk()
root.bind('<Escape>', lambda e: root.quit())
lmain = Label(root)
lmain.pack()
lProccessedData = Label(root)
lProccessedData.pack()
B = Button( text ="Hello", command = takePicture)
B.pack()
textEditor = Text(root, width=43, height=5)
textEditor.pack()
textEditor.place(x=400, y=400)

setImage=False
selectedImage=None
#lmain.config(width=300, height=300)
root.geometry("900x600")
root.resizable(False, False)


def set_count(products):
    div={"Harina de Trigo La Nieve":1700,"Papitas margarita":1000,"Lentejas":1800,"Shampoo":13900,"Tarrito rojo":13000,"Polvo de bizcocho":2000}
    div_temp=[]
    a=""
    b=0
    print(products)
    for item in products:
        if item in div_temp:
            continue
        div_temp.append(item)
        c=products.count(item)*div[item]
        b=b+c
        print (item)
        a=a+item+ "    "+str(products.count(item))+ "    " +str(c)+" \n"
    textEditor.insert('1.0', "")

    a=a+" \n\n\n Toral:"+str(b)+"\n\n"

    textEditor.insert('1.0', a)

def show_frame():
    global setImage
    global selectedImage
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    orig=cv2image
    img = PIL.Image.fromarray(cv2image)
    img=img.resize((400, 300))
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    if setImage:
        selectedImage=frame
        setImage = False
        cv2.imwrite('hola.jpg', selectedImage)
        res=control.get_results('hola.jpg')
        addRectangles(res[0])
        set_count(res[1])
        selectedImage=cv2.imread('result.png')
        selectedImage=PIL.Image.fromarray(selectedImage)
        selectedImage=selectedImage.resize((400, 300))
        imgtk = ImageTk.PhotoImage(image=selectedImage)
        selectedImage=imgtk
        B["state"] = NORMAL

    lmain.after(10, show_frame)
    lmain.place(x=10, y=40)
    B.place(x=10, y=500)
    lProccessedData.place(x=470, y=40)
    lProccessedData.configure(image=selectedImage)




show_frame()
root.mainloop()


