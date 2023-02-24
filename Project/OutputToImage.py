from PIL import Image, ImageDraw, ImageFont


def CreImg (ImgSiz):
    NewIm = Image.new("RGBA", ((ImgSiz*30),(ImgSiz*26)), color=(0,0,0))
    ImgDraw = ImageDraw.Draw(NewIm)
    global TriangleList
    TriangleList = []
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

    PointList = PointListCre(TriangleList)
    for triangle in TriangleList:
        ImgDraw.polygon((triangle[0]),(triangle[1]),outline=None)
    ImgDraw.polygon((PointList[18][1]),(0,0,0),outline=None)

    return(NewIm)

def ImgDra (ImgSiz, DLR, U, E, NewIm):
    ImgDraw = ImageDraw.Draw(NewIm)
    # U is upright, E is even, DLR is draw location row

    if DLR == 0:
        #First triangle (Top left)
        # ImgDraw.polygon(((0,0),(0,26),(15,26)),fill=(255,255,255),outline=None)
        TriangleList.append( [[(0,0),(0,26),(15,26)],(255,255,255)] )

        # ROW CREATE
        NewIm = RowCre (ImgSiz,DLR,E,U,NewIm,TriangleList)

        # Top right corner  
        # ImgDraw.polygon((((ImgSiz*30),0),((ImgSiz*30),26),((ImgSiz*30-15),26)),fill=(255,255,255),outline=None)
        TriangleList.append( [[((ImgSiz*30),0),((ImgSiz*30),26),((ImgSiz*30-15),26)], (255,255,255)] )
    else:
        if U == False:
            # Front side edge creation (up)
            # ImgDraw.polygon(((0,(DLR*26)),(0,(DLR*26)+26),(15,(DLR*26))),fill=(200,200,200),outline=None)
            TriangleList.append( [[(0,(DLR*26)),(0,(DLR*26)+26),(15,(DLR*26))], (200,200,200)] )

            # ROW CREATE
            NewIm = RowCre (ImgSiz,DLR,E,U,NewIm,TriangleList)

            # Back side edge creation (w/ front as up)
            # ImgDraw.polygon((((30*ImgSiz),(DLR*26)),((30*ImgSiz),(DLR*26)+26),((30*ImgSiz)-15,(DLR*26))),fill=(200,200,200),outline=None)
            TriangleList.append( [[((30*ImgSiz),(DLR*26)),((30*ImgSiz),(DLR*26)+26),((30*ImgSiz)-15,(DLR*26))], (200,200,200)] )

        else:
            # Front side edge creation (down)
            # ImgDraw.polygon(((0,(DLR*26)),(0,(DLR*26)+26),(15,(DLR*26)+26)),fill=(255,255,255),outline=None)
            TriangleList.append( [[(0,(DLR*26)),(0,(DLR*26)+26),(15,(DLR*26)+26)], (255,255,255)] )
            
            # ROW CREATE
            NewIm = RowCre (ImgSiz,DLR,E,U,NewIm,TriangleList)
            
            # Back side creation (w/ front as down)
            # ImgDraw.polygon((((30*ImgSiz),(DLR*26)),((30*ImgSiz),(DLR*26)+26),((30*ImgSiz)-15,(DLR*26)+26)),fill=(255,255,255),outline=None)
            TriangleList.append( [[((30*ImgSiz),(DLR*26)),((30*ImgSiz),(DLR*26)+26),((30*ImgSiz)-15,(DLR*26)+26)], (255,255,255)] )
    
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
            # ImgDraw.polygon(((i*30,RT),(i*30+15,RB),(i*30+30,RT)),fill=(200,200,200),outline=None)
            TriangleList.append( [[(i*30,RT),(i*30+15,RB),(i*30+30,RT)], (200,200,200)] )
            if E == True or (E == False and i+1 != ImgSiz):
                # ImgDraw.polygon(((i*30+15,RB),(i*30+30,RT),(i*30+45,RB)),fill=(255,255,255),outline=None)
                TriangleList.append( [[(i*30+15,RB),(i*30+30,RT),(i*30+45,RB)], (255,255,255)] )
        else:
            # ImgDraw.polygon(((i*30,RB),(i*30+15,RT),(i*30+30,RB)),fill=(255,255,255),outline=None)
            TriangleList.append( [[(i*30,RB),(i*30+15,RT),(i*30+30,RB)], (255,255,255)] )
            if E == True or (E == False and i+1 != ImgSiz):
                # ImgDraw.polygon(((i*30+15,RT),(i*30+30,RB),(i*30+45,RT)),fill=(200,200,200),outline=None)
                TriangleList.append( [[(i*30+15,RT),(i*30+30,RB),(i*30+45,RT)], (200,200,200)] )
        i+=1
    return(NewIm)

def PointListCre(TriangleList):
    PointList = []

    # adds every instance of every point and all relations

    # iterates through triangles in triangle list
    for triangle in TriangleList:
        # iterates through points in triangle
        for point in triangle[0]:
            ToAppend = point
            RelsList = []
            # iterates through the points in the same triangle again
            for othpoint in triangle[0]:
                # discards the point that is currently being appended
                if othpoint != point:
                    RelsList.append(othpoint)
            PointList.append( [ToAppend,RelsList] )
    
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
        TempPointList.append( [pointloc,[]] )

    # adds point relations to scaffolding
    for PointInfo in TempPointList:
        for point in PointList:
            if PointInfo[0] == point[0]:
                PointRelList = []
                for pointrel in point[1]:
                    PointInfo[1].append(pointrel)

    PointList = TempPointList

    # removes repeated related points in each point
    for pointinfo in PointList:
        TempRelationsList = []
        for relpoint in pointinfo[1]:
            if relpoint not in TempRelationsList:
                TempRelationsList.append(relpoint)
        pointinfo[1] = TempRelationsList
        
    return(PointList)

def TriangleListRefine(TriangleList, PointList):
    # iterates through triangles in triangle list
    for triangle in TriangleList:
        # iterates through the points in each triangle
        for point in triangle:
            # iterates through all points in pointlist
            i=0
            TriPointList = []
            while i<len.PointList:
                # looks for points present in triangle in the full points list
                if point == PointList[i]:
                    # notes index of points
                    TriPointList.append(i)
                i+=1
            #adds index of all points in the triangle to the triangle in the triangle list
            triangle.append(TriPointList)
    return(TriangleList)



CreImg(4).show()