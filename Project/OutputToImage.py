from PIL import Image, ImageDraw, ImageFont


def CreImg (ImgSiz):
    NewIm = Image.new("RGBA", ((ImgSiz*30),(ImgSiz*26)), color=(0,0,0))
    ImgFont = ImageFont.truetype(r'C:\Users\s_KermiWrigh41191\Documents\Code\Git Pages\KermitWright\Project\cutest_things\Cutest Things.ttf', 40)  
    ImgDraw = ImageDraw.Draw(NewIm)
    PointList = []
    TriangleList = []
    # Point dict is a dictionary of all points which can be warped to change the grid shape
    # Triangle dict is a dictionary of all triangles and their color
    # TID is Triangle ID, PID is point ID

    # V Input to Triangle creation functions V
    if ImgSiz % 2 == 0:
        i=ImgSiz
        U = True
        while i >= 1:
            NewIm = ImgDra(ImgSiz, (ImgSiz-i), U, True, NewIm, PointList, TriangleList)
            i-=1
            if U == False:
                U = True
            else:
                U = False
    elif ImgSiz % 2 != 0:
        i=ImgSiz
        U = True
        while i > 0:
            NewIm = ImgDra(ImgSiz, (ImgSiz-i), U, False, NewIm, PointList, TriangleList)
            i-=1
            if U == False:
                U = True
            else:
                U = False

    return(NewIm)

def ImgDra (ImgSiz, DLR, U, E, NewIm, PointList, TriangleList):
    ImgDraw = ImageDraw.Draw(NewIm)
    # U is upright, E is even, DLR is draw location row

    if DLR == 0:
        #First triangle (Top left)
        ImgDraw.polygon(((0,0),(0,26),(15,26)),fill=(255,255,255),outline=None)
        TriangleList.append( [[(0,0),(0,26),(15,26)],(255,255,255)] )
        PointList.append( [(0,0), ((30,0),(0,26),(15,26))] )

        # ROW CREATE
        NewIm = RowCre (ImgSiz,DLR,E,U,NewIm,PointList,TriangleList)

        # Top right corner  
        ImgDraw.polygon((((ImgSiz*30),0),((ImgSiz*30),26),((ImgSiz*30-15),26)),fill=(255,255,255),outline=None)
        TriangleList.append( [[((ImgSiz*30),0),((ImgSiz*30),26),((ImgSiz*30-15),26)], (255,255,255)] )
        PointList.append( [((ImgSiz*30),0), (((ImgSiz*30),26),((ImgSiz*30-15),26),((ImgSiz*30-30),0))] )
    else:
        if U == False:
            # Front side edge creation (up)
            ImgDraw.polygon(((0,(DLR*26)),(0,(DLR*26)+26),(15,(DLR*26))),fill=(200,200,200),outline=None)

            # ROW CREATE
            NewIm = RowCre (ImgSiz,DLR,E,U,NewIm,PointList,TriangleList)

            # Back side edge creation (w/ front as up)
            ImgDraw.polygon((((30*ImgSiz),(DLR*26)),((30*ImgSiz),(DLR*26)+26),((30*ImgSiz)-15,(DLR*26))),fill=(200,200,200),outline=None)
        else:
            # Front side edge creation (down)
            ImgDraw.polygon(((0,(DLR*26)),(0,(DLR*26)+26),(15,(DLR*26)+26)),fill=(255,255,255),outline=None)
            
            # ROW CREATE
            NewIm = RowCre (ImgSiz,DLR,E,U,NewIm,PointList,TriangleList)
            
            # Back side creation (w/ front as down)
            ImgDraw.polygon((((30*ImgSiz),(DLR*26)),((30*ImgSiz),(DLR*26)+26),((30*ImgSiz)-15,(DLR*26)+26)),fill=(255,255,255),outline=None)
    
    return(NewIm)

def RowCre (ImgSiz, DLR, E, U, NewIm, PointList, TriangleList):
    ImgDraw = ImageDraw.Draw(NewIm)
    RT = (DLR*26) 
    RB = (DLR*26) + 26
    # RT is row top, RB is row bottom

    i=0
    while i < ImgSiz:
        # draw triangles here
        if U == True:
            ImgDraw.polygon(((i*30,RT),(i*30+15,RB),(i*30+30,RT)),fill=(200,200,200),outline=None)
            if E == True or (E == False and i+1 != ImgSiz):
                ImgDraw.polygon(((i*30+15,RB),(i*30+30,RT),(i*30+45,RB)),fill=(255,255,255),outline=None)
        else:
            ImgDraw.polygon(((i*30,RB),(i*30+15,RT),(i*30+30,RB)),fill=(255,255,255),outline=None)
            if E == True or (E == False and i+1 != ImgSiz):
                ImgDraw.polygon(((i*30+15,RT),(i*30+30,RB),(i*30+45,RT)),fill=(200,200,200),outline=None)
        i+=1
    return(NewIm)


CreImg(10).show()