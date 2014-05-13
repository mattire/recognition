
import sys
import Image
import ImageFilter
import PIL.ImageOps
from SymmetryCalc import SymmetryCalc, ReferenceLimit
# from SymmetryCalc import ReferenceLimit

class AngleDetect:

    def __init__(self, image, reference):
        self.img = PIL.ImageOps.invert(image)
        self.rf = reference
        self.symlist = []
        
        
    def findRotationAngle(self):
        i = None
        for r in range(1,180):
            i = self.img.rotate(r, expand=1)
            # name = 'rot'+str(r)+'.png'
            # print name
            # i.save(name)

            sc = SymmetryCalc(i, self.rf, True)
            sym = sc.calcSymmetry()
            # sys.stdout.write(str(sym))
            # sys.stdout.write(' ')
            # print r
            self.symlist.append(sym)
            
        # print self.symlist
        return self.findBiggestSymmetry()
        
    def findBiggestSymmetry(self):
        angle = 0
        biggestSym=0
        # for i in range(1,360):
        for i in range(0,179):
            # print i
            sym = self.symlist[i]
            if(sym>biggestSym):
                biggestSym = sym
                angle = i-1
            
        return angle, biggestSym

    def correctRotation(self):
        a1, s1 = self.findRotationAngle()
        r1 = self.img.rotate(a1, expand=1)
        return r1
        
if __name__ == "__main__":
    img = Image.open('out2.png')
    imt = img.filter(ImageFilter.FIND_EDGES)
    imt.save('out5.png')
    # img2 = Image.open('out1.png')
    rf = ReferenceLimit(230,255)
    ad = AngleDetect(img, rf)
    # ad2 = AngleDetect(img2)
    
    a1, s1 = ad.findRotationAngle()
    print a1, s1
    
    # a2, s2 = ad2.findRotationAngle()
    print 'hello'
    #r1 = img.rotate(-a1, expand=1)
    img = PIL.ImageOps.invert(img)
    r1 = img.rotate(a1, expand=1)
    # r2 = img2.rotate(-a2, expand=1)
    
    r1.save('result1.png')
    # r2.save('result2.png')
    
