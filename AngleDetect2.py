
import sys
import Image
import ImageFilter
import PIL.ImageOps
import operator
from SymmetryCalc import SymmetryCalc, ReferenceLimit

class AngleDetect2:

    def __init__(self, image, reference):
        self.img = PIL.ImageOps.invert(image)
        self.rf = reference
        self.symlist = {}
        
        
    def findRotationAngle(self, min, max, step):
        i = None
        # first calc symmetry without rotation
        sc = SymmetryCalc(self.img, self.rf, True)
        sym = sc.calcSymmetry()
        self.symlist[0]=sym
            
        for r in xrange(min,max, step):
            i = self.img.rotate(r, expand=1)

            sc = SymmetryCalc(i, self.rf, True)
            sym = sc.calcSymmetry()
            # sys.stdout.write(str(sym))
            # sys.stdout.write(' ')
            # print r
            self.symlist[r]=sym
            
        # list = sorted(
            # self.symlist.iteritems(), 
            # key=operator.itemgetter(0))
        # print list
        
        rotation, bsym = self.findBiggestSymmetry()
        return rotation, bsym
        
    def findBiggestSymmetry(self):
        rotation = 0
        biggestSym=-1000
        for pair in self.symlist.items():
            if(pair[1]>biggestSym):
                biggestSym = pair[1]
                rotation = pair[0]
        return rotation, biggestSym

    def fineTune(self, step):
        
        pass
        
    def correctRotation(self):
        step1 = 10
        a1, s1 = self.findRotationAngle(step1,180, step1)
        a2, s2 = self.findRotationAngle(a1-step1,a1+step1, 1)
        r1 = self.img.rotate(a2, expand=1)
        return r1

        
        
        
# if __name__ == "__main__":
    # imgFile = "adTestIn.png"
    # img = Image.open(imgFile)
    # rf = ReferenceLimit(200,255)
    # ad = AngleDetect2(img, rf)
    # img2 = ad.correctRotation()
    # img2.save('adtest.png')
    
    