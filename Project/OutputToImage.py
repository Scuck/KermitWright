from PIL import Image, ImageDraw, ImageFont


def CreImg (ImgSiz):
    NewIm = Image.new("RGBA", ((ImgSiz*30),(ImgSiz*26)), color=(0,0,0))
    ImgDraw = ImageDraw.Draw(NewIm)
    global TriangleList
    TriangleList = []
    global PointList
    PointList = []
    # Point dict is a dictionary of all points which can be warped to change the grid shape
    # Triangle dict is a dictionary of all triangles and their color
    # TID is Triangle ID, PID is point ID

    # V Input to Triangle creation functions V
    if ImgSiz % 2 == 0:
        i=ImgSiz
        U = True
        while i >= 1:
            ImgDra(ImgSiz, (ImgSiz-i), U, True, NewIm)
            i-=1
            if U == False:
                U = True
            else:
                U = False

    elif ImgSiz % 2 != 0:
        i=ImgSiz
        U = True
        while i > 0:
            ImgDra(ImgSiz, (ImgSiz-i), U, False, NewIm)
            i-=1
            if U == False:
                U = True
            else:
                U = False

    PointList = PointListCre(PointList)
    for triangle in TriangleList:
        ImgDraw.polygon((triangle[0]),(triangle[1]),outline=None)

    return(NewIm)

def ImgDra (ImgSiz, DLR, U, E, NewIm):
    PointList = []
    # U is upright, E is even, DLR is draw location row

    if DLR == 0:
        #First triangle (Top left)
        TriangleCre([(0,0),(0,26),(15,26)],(255,255,255),PointList,TriangleList)

        # ROW CREATE
        NewIm = RowCre (ImgSiz,DLR,E,U,NewIm,TriangleList)

        # Top right corner  
        TriangleCre([((ImgSiz*30),0),((ImgSiz*30),26),((ImgSiz*30-15),26)],(255,255,255),PointList,TriangleList)
    else:
        if U == False:
            # Front side edge creation (up)
            TriangleCre([(0,(DLR*26)),(0,(DLR*26)+26),(15,(DLR*26))],(200,200,200),PointList,TriangleList)

            # ROW CREATE
            NewIm = RowCre (ImgSiz,DLR,E,U,NewIm,TriangleList)

            # Back side edge creation (w/ front as up)
            TriangleCre([((30*ImgSiz),(DLR*26)),((30*ImgSiz),(DLR*26)+26),((30*ImgSiz)-15,(DLR*26))],(200,200,200),PointList,TriangleList)

        else:
            # Front side edge creation (down)
            TriangleCre([(0,(DLR*26)),(0,(DLR*26)+26),(15,(DLR*26)+26)],(255,255,255),PointList,TriangleList)

            
            # ROW CREATE
            NewIm = RowCre (ImgSiz,DLR,E,U,NewIm,TriangleList)
            
            # Back side creation (w/ front as down)
            TriangleCre([((30*ImgSiz),(DLR*26)),((30*ImgSiz),(DLR*26)+26),((30*ImgSiz)-15,(DLR*26)+26)],(255,255,255),PointList,TriangleList)

    return(TriangleList)

def RowCre (ImgSiz, DLR, E, U, NewIm, TriangleList):
    ImgDraw = ImageDraw.Draw(NewIm)
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
    return(NewIm)

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

CreImg(12).show()