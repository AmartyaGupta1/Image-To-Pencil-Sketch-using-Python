from tkinter import *
from PIL import ImageTk, Image
import PIL.Image
import cv2



# Create an instance of tkinter window
win = Tk()

# Define the geometry of the window
win.geometry("1000x1000")
win.title("Converting Picture into Pencil Sketch")

img =cv2.imread("C:\\Users\\Amartya Gupta\\Pictures\\ABBEY.jpg")
half = cv2.resize(img, (750, 400))
blue,green,red = cv2.split(half)
half = cv2.merge((red,green,blue))
im = Image.fromarray(half)
imgtk = PIL.ImageTk.PhotoImage(image=im)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_invert = cv2.bitwise_not(img_gray)
img_smoothing = cv2.GaussianBlur(img_invert, (121, 121),sigmaX=0, sigmaY=0)
final = cv2.divide(img_gray,255-img_smoothing, scale=255)

half1 = cv2.resize(final, (750, 400))

photo = ImageTk.PhotoImage(image = PIL.Image.fromarray(half1))

Label(win, text=" INTO PENCIL SKETCH",font=40).grid(row=1,column=2,sticky = 'w' )
Label(win, text="CONVERSION OF PICTURE",font=40).grid(row=1,column=1,sticky = 'e' )
Label(win, text=" ",font=40).grid(row=2,column=2)
Label(win, text="INPUT IMAGE",font=50).grid(row=3,column=1)
Label(win, text="OUTPUT IMAGE",font=50).grid(row=3,column=2)
Label(win, image= imgtk).grid(row=4,column=1)
Label(win, image=photo).grid(row=4,column=2)
Label(win, text=" ",font=40).grid(row=5,column=2)
Label(win, text=" ",font=40).grid(row=6,column=2)
Label(win, text=" ",font=40).grid(row=7,column=2)



win.mainloop()
