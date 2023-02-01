from PIL import Image, ImageDraw, ImageFont

NewIm = Image.new("RGBA", (560,560), color=(0,0,0))
ImgFont = ImageFont.truetype(r'C:\Users\s_KermiWrigh41191\Documents\Code\Git Pages\KermitWright\Project\cutest_things\Cutest Things.ttf', 40)  
ImgDraw = ImageDraw.Draw(NewIm)
ImgDraw.text((12,8), "Text that I am \n writing",font=ImgFont, fill=(255,255,255,255))
ImgDraw.line((200,150,300,200),fill=(255,255,100),width=10)
ImgDraw.polygon(((400,300),(300,200),(500,50)),fill=(255,0,0),outline=None)
NewIm.show()