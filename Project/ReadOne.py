import PIL
ImgFileObject = open(r"Project\TESTFILE.txt", "r")
ImgRawData = ImgFileObject.read()
ImgFileObject.close()

ImgDataList = ImgRawData.split(":")
i=0
while i < len(ImgDataList):
    ImgDataList[i] = ImgDataList[i].split(";")
    i+=1
ImgSpecs = ImgDataList[0]
ImgDataList.pop(0)
print(ImgSpecs)
print(ImgDataList)