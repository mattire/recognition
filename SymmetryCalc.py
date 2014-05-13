
import Image
import PIL.ImageOps
import helputil

# relevant brightness area to be compared
# when calculating symmetry
class ReferenceLimit:
    def __init__(self, pmin, pmax):
        self.max=pmax
        self.min=pmin

class SymmetryCalc:
    
    def __init__(self):
        pass
        
    def __init__(self, image, reference, weightedCenter=False):
        self.img=image
        self.centerX = self.img.size[0]/2
        self.height = self.img.size[1]
        self.remainder = self.img.size[0]%2
        self.x1s = 0
        self.x2s = 0
        self.rf = reference
        self.wCntr = weightedCenter
        if(self.wCntr):
            self.setupWCenter()
        

    def setImage(self, image, reference, weightedCenter=False):
        self.img = image
        self.centerX = self.img.size[0]/2
        self.height = self.img.size[1]
        self.remainder = self.img.size[0]%2
        self.x1s = 0
        self.x2s = 0
        self.rf = reference
        self.wCntr = weightedCenter
        if(self.wCntr):
            setupWCenter()

    def setupWCenter(self):
        self.wCenter = helputil.calcWeightedCenterX(self.img, self.rf.min, self.rf.max)
        
    def calcSymmetry(self):
        self.decideStartPoints()
        
        symSum = 0
        for y in range(0, self.height):
            # symSum += self.calcRowSymmetry(y)
            sym = self.calcRowSymmetry(y)
            # print sym
            symSum += sym
        
        return symSum

    def decideStartPoints(self):
        x1start=0
        x2start=0
        if(not(self.wCntr)):
            if(self.remainder==0):
                x1start=self.centerX
                x2start=self.centerX+1
            else:
                x1start=self.centerX-1
                x2start=self.centerX+1
        else:
            x1start=self.wCenter
            x2start=self.wCenter+1            
            
        self.x1s = x1start
        self.x2s = x2start
        
    def calcRowSymmetry(self, y):
        sum=0
        center = 0
        #half = self.img.size[0]/2 - 1
        half = self.decideSymmetryCalcLength()
        if(not(self.wCntr)):
            center = self.centerX
        else:
            center = self.wCenter
        
        for i in range(0, half):
            pxl1 = self.img.getpixel((center-i,y))
            pxl2 = self.img.getpixel((center+i,y))
            sum += self.comparePixels(pxl1,pxl2)
        return sum
    
    def decideSymmetryCalcLength(self):
        if(not(self.wCntr)):
            return self.img.size[0]/2 - 1
        else:
            distanceToEnd = abs(self.wCenter - self.img.size[0])
            # return the shorter distance:
            if(distanceToEnd<self.wCenter):
                # print distanceToEnd
                return distanceToEnd
            else:
                # print self.wCenter
                return self.wCenter
            
    
    def comparePixels(self,pxl1,pxl2):
        tolerance = 10
        if(self.referenceAreaCheck(pxl1)):
            for i in range(0,2):
                if (pxl1[i] > pxl2[i] + tolerance or 
                    pxl1[i] < pxl2[i] - tolerance):
                    # print '-1'
                    return -1
            return 1
        else:
            return 0
        
    def referenceAreaCheck(self, pxl):
        for i in range(0,2):
            if(pxl[i]>self.rf.max or pxl[i]<self.rf.min):
                return False
        return True
    
if __name__ == "__main__":

    #rf = ReferenceLimit(0,120)
    rf = ReferenceLimit(230,255)
    
    img = Image.open('out.png')
    img2 = Image.open('out2.png')
    
    img = PIL.ImageOps.invert(img)
    img2 = PIL.ImageOps.invert(img2)
    
    #sc = SymmetryCalc(img, rf)
    sc = SymmetryCalc(img, rf, True)
    # sc2 = SymmetryCalc(img2, rf)
    sc2 = SymmetryCalc(img2, rf, True)
    #print sc
    print sc.calcSymmetry()
    print sc2.calcSymmetry()
