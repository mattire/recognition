
def calcWeightedCenterX(img, min, max):
    list = readImagePixelsWithinLimit(img, min, max)
    sumX = 0
    for i in list:
        sumX += i[0]
    return sumX/len(list)

def cropImage(img, min, max):
    list = readImagePixelsWithinLimit(img, min, max)
    # print list
    maxX, minX = findBiggestAndSmallest(list, 0, img.size[0],0)
    maxY, minY = findBiggestAndSmallest(list, 1, img.size[1],0)
    print minX,minY,maxX,maxY
    img2 = img.crop((minX,minY,maxX,maxY))
    return img2


def findBiggestAndSmallest(l, ind, startmin, startmax):
    biggest=startmax
    smallest=startmin
    for item in l:
        num = item[ind]
        if(num>biggest):
            biggest=num
        elif(num<smallest):
            smallest=num
            
    return (biggest,smallest)

    
def readImagePixelsWithinLimit(img, min, max):
    resultPixels=[]
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if(pixelInLimit(img.getpixel((i,j)), min, max)):
                # if(j==0):
                    # print 'add ' + str(i) + ' ' + str(j)
                resultPixels.append((i,j)) 
    return resultPixels

    
def pixelInLimit(pxl, min, max):
    for i in pxl:
        # print i
        if(i>max or i<min):
            # print 'f'
            return False
    return True

    
if __name__ == "__main__":
    img = Image.open('rot23.png')
    #img2 = cropImage(img, 0, 100)
    cx = calcWeightedCenterX(img, 100,255)
    print cx
    img2 = cropImage(img, 100, 255)
    img2.save('hu.png')
    
