
import Image

class Comparison:

    def __init__(self, pDbImg, pRefImg):
        self.imgDb = pDbImg
        self.imgRef = pRefImg
        self.similarity = 0 
        self.compare()
        
        
    def compare(self):
        
        simPoints = 0
        difPoints = 0
        totalAmount = 0
        
        dbStartX = 0
        refStartX = 0
        width = 0
        dbW = self.imgDb.size[0]
        refW = self.imgRef.size[0]
        
        if(dbW>refW):
            width = refW
            refStartX = 0
            dbStartX = (dbW-refW)/2
        else:
            width = dbW
            dbStartX = 0
            refStartX = (refW-dbW)/2
        
        for j in range(0, self.imgDb.size[1]):
            for i in range(0, width):
                y = j
                x = dbStartX + i
                refB = self.pixelIsDark(self.imgDb, x, y)
                x = refStartX + i
                dbB = self.pixelIsDark(self.imgRef, x, y)
                if(refB==dbB):
                    simPoints+=1
                else:
                    difPoints+=1
        # print simPoints/float(simPoints+difPoints)
        self.similarity = simPoints/float(simPoints+difPoints)
        
    def getCoords(self, ):
        return x, y
        
    def pixelIsDark(self, img, x, y):
        pxl = img.getpixel((x,y))
        limit = 20
        for i in pxl:
            if i > limit:
                return False
        return True