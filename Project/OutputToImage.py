from PIL import Image, ImageDraw, ImageFont

def CreImg (ImgSiz):
    NewIm = Image.new("RGBA", ((ImgSiz*30),(ImgSiz*26)), color=(0,0,0))
    ImgFont = ImageFont.truetype(r'C:\Users\s_KermiWrigh41191\Documents\Code\Git Pages\KermitWright\Project\cutest_things\Cutest Things.ttf', 40)  
    ImgDraw = ImageDraw.Draw(NewIm)
    ImgDraw.polygon(((0,0),(0,26),(15,26)),fill=(255,255,255),outline=None)
    ImgDraw.polygon((((ImgSiz*30),(ImgSiz*26)),((ImgSiz*30),(ImgSiz*26)-26),((ImgSiz*30)-15,(ImgSiz*26)-26)),fill=(200,200,200),outline=None)
    if ImgSiz % 2 == 0:
        ImgDraw.polygon((((ImgSiz*30),0),((ImgSiz*30),26),((ImgSiz*30-15),26)),fill=(255,255,255),outline=None)
        ImgDraw.polygon(((0,(ImgSiz*26)),(0,(ImgSiz*26)-26),(15,(ImgSiz*26)-26)),fill=(200,200,200),outline=None)

        i=ImgSiz
        U = False
        while i > 1:
            i-=1
            NewIm = EdgCre(ImgSiz, (ImgSiz-i), U, True, NewIm)
            if U == False:
                U = True
            else:
                U = False

    elif ImgSiz % 2 != 0:
        ImgDraw.polygon((((ImgSiz*30),0),((ImgSiz*30),26),((ImgSiz*30-15),0)),fill=(200,200,200),outline=None)
        ImgDraw.polygon(((0,(ImgSiz*26)),(0,(ImgSiz*26)-26),(15,(ImgSiz*26))),fill=(255,255,255),outline=None)

        i=ImgSiz
        U = False
        while i > 1:
            i-=1
            NewIm = EdgCre((ImgSiz-i), U, False, NewIm)
            if U == False:
                U = True
            else:
                U = False

    return(NewIm)

def EdgCre (ImgSiz, DL, U, E, NewIm):
    ImgDraw = ImageDraw.Draw(NewIm)
    if U == False:
        ImgDraw.polygon(((0,(DL*26)),(0,(DL*26)+26),(15,(DL*26))),fill=(200,200,200),outline=None)
        # V This part isnt done yet V
        if E == True:
            ImgDraw.polygon((((30*ImgSiz),(DL*26)),(0,(DL*26)+26),(15,(DL*26))),fill=(200,200,200),outline=None)
        else:
            ImgDraw.polygon(((0,(DL*26)),(0,(DL*26)+26),(15,(DL*26))),fill=(200,200,200),outline=None)
        # ^ ^
    else:
        ImgDraw.polygon(((0,(DL*26)),(0,(DL*26)+26),(15,(DL*26)+26)),fill=(255,255,255),outline=None)
    return(NewIm)



CreImg(4).show()