from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from PIL import ImageTk as itk, Image, ImageDraw

FClickCo = [0,0]
SClickCo = [0,0]
ClickQ = True
ToolSelected = 'Warp'

Win1 = Tk()
Win1.geometry("800x800")
Win1Lab = Label(text="V Image Goes Here V",foreground="purple")
Win1Lab.pack()

DefaultImgPil = Image.open(r"Project\Cryptotora.JPG")
DefaultImg = itk.PhotoImage(DefaultImgPil)

# IMG CREATION STUFF v v v

# Create Images
def CreImg (ImgSiz):
    global NewIm
    NewIm = Image.new("RGBA", ((ImgSiz*30),(ImgSiz*26)), color=(0,0,0))
    global TriangleList
    global PointList
    TriangleList = []
    PointList = []
    # Point list is a list of all points and all other points and triangles that those points are related to
    # Triangle list is a list of all triangles and their color
    # TID is Triangle ID, PID is point ID

    # V Input to Triangle creation functions V
    if ImgSiz % 2 == 0:
        i=ImgSiz
        U = True
        while i >= 1:
            ImgDra(ImgSiz, (ImgSiz-i), U, True)
            i-=1
            if U == False:
                U = True
            else:
                U = False

    elif ImgSiz % 2 != 0:
        i=ImgSiz
        U = True
        while i > 0:
            ImgDra(ImgSiz, (ImgSiz-i), U, False)
            i-=1
            if U == False:
                U = True
            else:
                U = False

    PointList = PointListCre(PointList)

    ImgDraw = ImageDraw.Draw(NewIm)
    for triangle in TriangleList:
        ImgDraw.polygon((triangle[0]),(triangle[1]),outline=None)

    return (NewIm)

def ImgDra (ImgSiz, DLR, U, E):
    PointList = []
    # U is upright, E is even, DLR is draw location row

    if DLR == 0:
        #First triangle (Top left)
        TriangleCre([(0,0),(0,26),(15,26)],(255,255,255),PointList,TriangleList)

        # ROW CREATE
        RowCre (ImgSiz,DLR,E,U,TriangleList)

        # Top right corner  
        TriangleCre([((ImgSiz*30),0),((ImgSiz*30),26),((ImgSiz*30-15),26)],(255,255,255),PointList,TriangleList)
    else:
        if U == False:
            # Front side edge creation (up)
            TriangleCre([(0,(DLR*26)),(0,(DLR*26)+26),(15,(DLR*26))],(200,200,200),PointList,TriangleList)

            # ROW CREATE
            RowCre (ImgSiz,DLR,E,U,TriangleList)

            # Back side edge creation (w/ front as up)
            TriangleCre([((30*ImgSiz),(DLR*26)),((30*ImgSiz),(DLR*26)+26),((30*ImgSiz)-15,(DLR*26))],(200,200,200),PointList,TriangleList)

        else:
            # Front side edge creation (down)
            TriangleCre([(0,(DLR*26)),(0,(DLR*26)+26),(15,(DLR*26)+26)],(255,255,255),PointList,TriangleList)

            
            # ROW CREATE
            RowCre (ImgSiz,DLR,E,U,TriangleList)
            
            # Back side creation (w/ front as down)
            TriangleCre([((30*ImgSiz),(DLR*26)),((30*ImgSiz),(DLR*26)+26),((30*ImgSiz)-15,(DLR*26)+26)],(255,255,255),PointList,TriangleList)

    return(TriangleList)

def RowCre (ImgSiz, DLR, E, U, TriangleList):
    RT = (DLR*26) 
    RB = (DLR*26) + 26
    # RT is row top, RB is row bottom

    i=0
    while i < ImgSiz:
        # draw triangles here
        if U == True:
            TriangleCre([(i*30,RT),(i*30+15,RB),(i*30+30,RT)],(200,200,200),PointList,TriangleList)

            if E == True or (E == False and i+1 != ImgSiz):
                TriangleCre([(i*30+15,RB),(i*30+30,RT),(i*30+45,RB)],(255,255,255),PointList,TriangleList)

        else:
            TriangleCre([(i*30,RB),(i*30+15,RT),(i*30+30,RB)],(255,255,255),PointList,TriangleList)
            if E == True or (E == False and i+1 != ImgSiz):
                TriangleCre([(i*30+15,RT),(i*30+30,RB),(i*30+45,RT)],(200,200,200),PointList,TriangleList)
        i+=1

def TriangleCre( CoordsList,Color,PointList,TriangleList ):
    for point in CoordsList:
        ToAppend = point
        RelsList = []
        # iterates through the points in the same triangle again
        for othpoint in CoordsList:
            # discards the point that is currently being appended
            if othpoint != point:
                RelsList.append(othpoint)
        PointList.append( [ToAppend,RelsList,[]] )
        PointList[-1][2].append(len(TriangleList))
    TriangleList.append([CoordsList,Color])

def PointListCre(PointList):    
    # creates a list of the locations of points
    PointIndexList = []
    for point in PointList:
        PointIndexList.append(point[0])

    # creates list of non-repeated point 
    TruePointListReference = []
    # Iterates through all points in point list
    for pointloc in PointIndexList:
        # checks if point has already been put in the reference list / adds it
        if pointloc not in TruePointListReference:
            TruePointListReference.append(pointloc)

    # Makes list scaffolding
    TempPointList = []
    for pointloc in TruePointListReference:
        TempPointList.append( [pointloc,[],[]] )

    # adds point relations to scaffolding
    for PointInfo in TempPointList:
        for point in PointList:
            if PointInfo[0] == point[0]:
                for pointrel in point[1]:
                    PointInfo[1].append(pointrel)
                # adds triangle relations (there is only 1 triangle in each triangle instance, so you only need to append the 1)
                PointInfo[2].append(point[2][0])

    PointList = TempPointList

    # removes repeated related points in each point
    for pointinfo in PointList:
        TempRelationsList = []
        for relpoint in pointinfo[1]:
            if relpoint not in TempRelationsList:
                TempRelationsList.append(relpoint)
        pointinfo[1] = TempRelationsList
        
    return(PointList)

# IMG CREATION STUFF ^ ^ ^

# Update Image
def ImgRender():
    ImgDraw = ImageDraw.Draw(NewIm)
    for triangle in TriangleList:
        ImgDraw.polygon((triangle[0]),(triangle[1]),outline=None)
   
    return(NewIm)

# Interface stuff

# CLICKABLE FISH!!!!!
def CursorFind(event):
    global FClickCo 
    global SClickCo 
    global ClickQ 
    global PointSelectData
    if ToolSelected == 'Warp':
        if ClickQ == True:
            FClickCo = (event.x , event.y)
            PointSelectData = PointSelect(FClickCo)
            if PointSelectData != None:
                ClickQ = False
        elif ClickQ == False:
            PointSelected = PointSelectData[0]
            PointSelectedInd = PointSelectData[1]
            SClickCo = (event.x , event.y)
            ClickQ = True
            for triangle in PointSelected[2]:
                TriInd = 0
                for point in TriangleList[triangle][0]:
                    if point == PointSelected[0]:
                        TriangleList[triangle][0][TriInd] = SClickCo
                    TriInd += 1
            PointList[PointSelectedInd][0] = SClickCo
            DispImg = itk.PhotoImage(ImgRender())
            DispBox.configure(image=DispImg)
            DispBox.image=DispImg
            DispBox.pack()
    elif ToolSelected == 'Color':
        CClickCo = (event.x , event.y)
        try:
            ColorSelected = (int(CSRed.get()),int(CSGreen.get()),int(CSBlue.get()))
        except:
            ColorSelected = (0,0,0)
        for triangle in TriangleList:
            TTriArea = abs( triangle[0][0][0] * ( triangle[0][1][1] - triangle[0][2][1] ) + triangle[0][1][0] * ( triangle[0][2][1] - triangle[0][0][1] ) + triangle[0][2][0] * (triangle[0][0][1] - triangle[0][1][1] ) )
            FTriArea = abs( CClickCo[0] * ( triangle[0][1][1] - triangle[0][2][1] ) + triangle[0][1][0] * ( triangle[0][2][1] - CClickCo[1] ) + triangle[0][2][0] * (CClickCo[1] - triangle[0][1][1] ) )
            STriArea = abs( triangle[0][0][0] * ( CClickCo[1] - triangle[0][2][1] ) + CClickCo[0] * ( triangle[0][2][1] - triangle[0][0][1] ) + triangle[0][2][0] * (triangle[0][0][1] - CClickCo[1] ) )
            ThTriArea = abs( triangle[0][0][0] * ( triangle[0][1][1] - CClickCo[1] ) + triangle[0][1][0] * ( CClickCo[1] - triangle[0][0][1] ) + CClickCo[0] * (triangle[0][0][1] - triangle[0][1][1] ) )
            if TTriArea >= (FTriArea + STriArea + ThTriArea):
                triangle[1] = ColorSelected
            DispImg = itk.PhotoImage(ImgRender())
            DispBox.configure(image=DispImg)
            DispBox.image=DispImg
            DispBox.pack()
        


def PointSelect(ClickCo):
    for point in PointList:
        if ((((ClickCo[0]-point[0][0])**2+(ClickCo[1]-point[0][1])**2)**(1/2)))<5:
            return(point,PointList.index(point))


# Image Creation Specs
ImgCreSiz = Entry(Win1)
ImgCreSiz.pack()

# Create Image Frame
ImgBox = Frame(Win1,width=600,height=600)
ImgBox.pack()
ImgBox.place(anchor='center', relx=0.5, rely=0.5)

DispBox = Label(ImgBox,image= DefaultImg) 
DispBox.bind("<Button-1>", CursorFind)
DispBox.pack()

# create button that generates a new image
def PreImgCre():
    try:
        DispImgPil = CreImg(int(ImgCreSiz.get()))
        DispImg = itk.PhotoImage(DispImgPil)
        DispBox.configure(image=DispImg)
        DispBox.image=DispImg
    except ValueError:
        pass

ImgCreFin = Button(Win1, text='Generate Image', command=PreImgCre)
ImgCreFin.pack()

# Image Coloring Specs
ColorSpecs = Frame(Win1)
CSRed = Entry(ColorSpecs)
CSGreen = Entry(ColorSpecs)
CSBlue = Entry(ColorSpecs)
ColorSpecs.pack()
CSRed.pack(side=LEFT)
CSGreen.pack(side=LEFT)
CSBlue.pack(side=LEFT)

# Create Tool Selection Button
def ToolSelect():
    global ToolSelected
    if ToolSelected == 'Color':
        ToolSelected = 'Warp'
    else:
        ToolSelected = 'Color'
    
ToolSwitch = Button(Win1, text='Switch Tools', command=ToolSelect)
ToolSwitch.pack()

# Make it Work
Win1.mainloop()