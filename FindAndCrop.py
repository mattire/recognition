
import Image
import PIL.ImageOps

def readImageBlackPixels(img):
    blackPixels=[]
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if(pixelNonWhite(img.getpixel((i,j)))):
                blackPixels.append((i,j)) 
    return blackPixels

def pixelNonWhite(pxl):
    limit = 240
    for i in pxl:
        if(i<220):
            return True
    return False
    
def getCenter(l):
    count = len(l)
    sumX=0
    sumY=0
    for item in l:
        sumX += item[0]
        sumY += item[1]
    aveX = sumX/count
    aveY = sumY/count
    return (aveX,aveY)
    
def findBiggestAndSmallest(l, ind, max, min):
    biggest=min
    smallest=max
    for item in l:
        num = item[ind]
        if(num>biggest):
            biggest=num
        elif(num<smallest):
            smallest=num
            
    return (biggest,smallest)
    
def invertFindAndCropImg(img):
    invImg = PIL.ImageOps.invert(img)
    return findAndCropImg(invImg)
    
def findAndCropImg(img):
    l = readImageBlackPixels(img)
    maxX, minX = findBiggestAndSmallest(l, 0, img.size[0],0)
    maxY, minY = findBiggestAndSmallest(l, 1, img.size[1],0)
    return img.crop((minX,minY,maxX,maxY+1))
    
    
def findAndCrop(imgName):
    img = Image.open(imgName)
    return findAndCropImg(img)            
            
# if __name__ == "__main__":
    # img = Image.open('test2.jpg')
    # l = readImageBlackPixels(img)
    
    # print getCenter(l)
    
    # maxX, minX = findBiggestAndSmallest(l, 0, img.size[0],0)
    # maxY, minY = findBiggestAndSmallest(l, 1, img.size[1],0)
    
    # print maxX, minX
    # print maxY, minY
    
    # img2 = img.crop((minX,minY,maxX,maxY+1))
    # img2.save('out2.png')