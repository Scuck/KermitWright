from PIL import Image, ImageDraw, ImageFont

def CreImg (ImgSiz):
    NewIm = Image.new("RGBA", ((ImgSiz*30),(ImgSiz*26)), color=(0,0,0))
    ImgFont = ImageFont.truetype(r'C:\Users\s_KermiWrigh41191\Documents\Code\Git Pages\KermitWright\Project\cutest_things\Cutest Things.ttf', 40)  
    ImgDraw = ImageDraw.Draw(NewIm)

    # V Input to Triangle creation functions V
    if ImgSiz % 2 == 0:
        i=ImgSiz
        U = True
        while i >= 1:
            NewIm = ImgCre(ImgSiz, (ImgSiz-i), 0, U, True, NewIm)
            i-=1
            if U == False:
                U = True
            else:
                U = False
    elif ImgSiz % 2 != 0:
        i=ImgSiz
        U = True
        while i > 0:
            NewIm = ImgCre(ImgSiz, (ImgSiz-i), 0, U, False, NewIm)
            i-=1
            if U == False:
                U = True
            else:
                U = False

    return(NewIm)

def ImgCre (ImgSiz, DLR, U, E, NewIm):
    ImgDraw = ImageDraw.Draw(NewIm)
    PointDict = {}
    TriangleDict = {}
    TID = 0
    R = 1
    # U is upright, E is even, DLR is draw location row, DLC is draw location column
    # Point dict is a dictionary of all points which can be warped to change the grid shape
    # Triangle dict is a dictionary of all triangles and their color
    # TID is Triangle ID



    if DLR == 0:
        #First triangle (Top left)
        ImgDraw.polygon(((0,0),(0,26),(15,26)),fill=(255,255,255),outline=None)
        if E == True: 
            # Top right corner even 
            ImgDraw.polygon((((ImgSiz*30),0),((ImgSiz*30),26),((ImgSiz*30-15),26)),fill=(255,255,255),outline=None)
        else:
            # Top right corner odd
            ImgDraw.polygon((((ImgSiz*30),0),((ImgSiz*30),26),((ImgSiz*30-15),0)),fill=(200,200,200),outline=None)
    elif DLR == ImgSiz:
        if E == True: 
            # bottom left corner even 
            ImgDraw.polygon(((0,(ImgSiz*26)),(0,(ImgSiz*26)-26),(15,(ImgSiz*26)-26)),fill=(200,200,200),outline=None)        
        else:
            # bottom left corner odd
            ImgDraw.polygon(((0,(ImgSiz*26)),(0,(ImgSiz*26)-26),(15,(ImgSiz*26)-26)),fill=(200,200,200),outline=None)
        #Final triangle (bottom right)
        ImgDraw.polygon((((ImgSiz*30),(ImgSiz*26)),((ImgSiz*30),(ImgSiz*26)-26),((ImgSiz*30)-15,(ImgSiz*26)-26)),fill=(200,200,200),outline=None)
    else:
        if U == False:
            # Front side edge creation (up)
            ImgDraw.polygon(((0,(DLR*26)),(0,(DLR*26)+26),(15,(DLR*26))),fill=(200,200,200),outline=None)
            if E == True:
            # Back side edge creation (w/ front as up)
                ImgDraw.polygon((((30*ImgSiz),(DLR*26)),((30*ImgSiz),(DLR*26)+26),((30*ImgSiz)-15,(DLR*26))),fill=(200,200,200),outline=None)
            else:
                ImgDraw.polygon((((30*ImgSiz),(DLR*26)),((30*ImgSiz),(DLR*26)+26),((30*ImgSiz)-15,(DLR*26)+26)),fill=(255,255,255),outline=None)
        else:
            # Front side edge creation (down)
            ImgDraw.polygon(((0,(DLR*26)),(0,(DLR*26)+26),(15,(DLR*26)+26)),fill=(255,255,255),outline=None)
            if E == True:
                # Back side edge creation (w/ front as down)
                ImgDraw.polygon((((30*ImgSiz),(DLR*26)),((30*ImgSiz),(DLR*26)+26),((30*ImgSiz)-15,(DLR*26)+26)),fill=(255,255,255),outline=None)
            else:
                ImgDraw.polygon((((30*ImgSiz),(DLR*26)),((30*ImgSiz),(DLR*26)+26),((30*ImgSiz)-15,(DLR*26))),fill=(200,200,200),outline=None)

    return(NewIm)



CreImg(2).show()