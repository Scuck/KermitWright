from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from PIL import ImageTk, Image
Win1 = Tk()
Win1.geometry("800x800")
Win1Lab = Label(text="V Image Goes Here V",foreground="purple")
Win1Lab.pack()

# Create Images
RawImg = ImageTk.PhotoImage(Image.open(r"Project\Cryptotora.JPG"))
ButtImg = ImageTk.PhotoImage(Image.new("RGBA", (600,600), color=(0,0,0,0)))

# Button Function
def ButtonPress():
    messagebox.showinfo("Button Box", "Button Pressed")

def CursorFind(event):
    Cursorx= event.x 
    Cursory= event.y
    print("Clicked!", f"{Cursorx},{Cursory}")

# Create Image Frame
ImgBox = Frame(Win1,width=600,height=600)
ImgBox.pack()
ImgBox.place(anchor='center', relx=0.5, rely=0.5)
#Place Image in Display Frame
ImgCont = Label(ImgBox, image = RawImg)
ImgCont.bind("<Button-1>", CursorFind)
ImgCont.pack()

# Create Click box
# ClickBox = Canvas(Win1, width=600, height=600)
# ClickBox.bind("<Button-1>", CursorFind)
# ClickBox.pack()
# ClickBox.place(anchor='center', relx=0.5, rely=0.5)


# Make it Work
Win1.mainloop()