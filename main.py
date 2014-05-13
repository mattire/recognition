
import sys


import FindAndCrop
from AngleDetect import AngleDetect
from AngleDetect2 import AngleDetect2
from SymmetryCalc import ReferenceLimit
from InsectImageDB import InsectImageDB
import time


# works only with images with one bug in them

if __name__ == "__main__":
    
    start = time.time()
    imgFile = "webTestImages/search4.jpg"
    name = ""
    if(len(sys.argv)==2):
        imgFile = sys.argv[1]
        name = imgFile.split('/')[len(imgFile.split('/'))-1].split('.')[0]
        
    # find black bug from image and cut it
    img = FindAndCrop.findAndCrop(imgFile)
    
    # rotate it 
    rf = ReferenceLimit(200,255)
    ad = AngleDetect2(img, rf)
    #ad = AngleDetect(img, rf)
    rImg = ad.correctRotation()

    # crop it again
    cImg = FindAndCrop.invertFindAndCropImg(rImg)
    
    # scale it
    iidb = InsectImageDB()
    sImg = iidb.resizeToStandardSize(cImg)
    # sImg.save(name+'_scaled.png')
    
    # compare it
    searchResult = iidb.find(sImg)
    print ''
    print searchResult
    
    
    end = time.time()
    diff = end-start
    
    print 'query length in seconds:'
    print diff
    