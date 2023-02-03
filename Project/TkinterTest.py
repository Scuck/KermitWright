from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from PIL import ImageTk, Image, ImageDraw

global FClickCo 
global SClickCo 
global ClickQ 
FClickCo = [0,0]
SClickCo = [0,0]
ClickQ = True

Win1 = Tk()
Win1.geometry("800x800")
Win1Lab = Label(text="V Image Goes Here V",foreground="purple")
Win1Lab.pack()

# Create Images
RawImg = ImageTk.PhotoImage(Image.open(r"Project\Cryptotora.JPG"))
ButtImg = ImageTk.PhotoImage(Image.new("RGBA", (600,600), color=(0,0,0,0)))
def CreateImage():
    ImgSiz = int(ImgCreSiz.get())
    NewImg = ImageTk.PhotoImage(Image.new("RGBA", ((ImgSiz*30),(ImgSiz*30)), color=(0,0,0,0)))
    # Triangles (on Creation) have a side length of 30 and a height of 26.
    ImgCre = ImageDraw.Draw(NewImg)
    ImgCre.polygon((0,0),(0,26),(15,26),fill=(255,255,255),outline=None)
    ImgCre.polygon((((ImgSiz*30),0),((ImgSiz*30),26),((ImgSiz*30-15),26)),fill=(255,255,255))


# CLICKABLE FISH!!!!!
def CursorFind(event):
    global FClickCo 
    global SClickCo 
    global ClickQ 
    if ClickQ == True:
        FClickCo[0] = event.x
        FClickCo[1] = event.y
        ClickQ = False
        print("First Click At:", f"{FClickCo}")
    else:
        SClickCo[0] = event.x 
        SClickCo[1] = event.y
        ClickQ = True
        print("Second Click At:", f"{SClickCo}")

# Image Creation Specs
ImgCreSiz = Entry(Win1)
ImgCreSiz.pack()
ImgCreFin = Button(Win1, text='Generate Image', command=CreateImage)
ImgCreFin.pack()

# Create Image Frame
ImgBox = Frame(Win1,width=600,height=600)
ImgBox.pack()
ImgBox.place(anchor='center', relx=0.5, rely=0.5)
#Place Image in Display Frame
ImgCont = Label(ImgBox, image = RawImg)
ImgCont.bind("<Button-1>", CursorFind)
ImgCont.pack()

# Make it Work
Win1.mainloop()