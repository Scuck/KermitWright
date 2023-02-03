from PIL import Image, ImageDraw, ImageFont

ImgSiz = 10
NewIm = Image.new("RGBA", ((ImgSiz*30),(ImgSiz*30)), color=(0,0,0))
ImgFont = ImageFont.truetype(r'C:\Users\s_KermiWrigh41191\Documents\Code\Git Pages\KermitWright\Project\cutest_things\Cutest Things.ttf', 40)  
ImgDraw = ImageDraw.Draw(NewIm)
ImgDraw.polygon(((0,0),(0,26),(15,26)),fill=(255,255,255),outline=None)
ImgDraw.polygon((((ImgSiz*30),0),((ImgSiz*30),26),((ImgSiz*30-15),26)),fill=(255,255,255))
NewIm.show()