

import Image
import FindAndCrop
from Comparison import Comparison
from os import walk
import os

BUG_DB_FOLDER = "bugDB"

LOAD_BUG_IMG_FOLDER = "origBugs"

class InsectImageDB:
    
    def __init__(self):
        # load images
        self.bugList = {}
        f = []
        for (dirpath, dirnames, filenames) in walk(BUG_DB_FOLDER):
            f.extend(filenames)
        
        for name in f:
            p = BUG_DB_FOLDER + os.sep + name
            img = Image.open(p)
            self.bugList[name]=img
        
    def getStandardImageHeight(self):
        return 150
        
    def resizeToStandardSize(self, img):
        stdHeight = self.getStandardImageHeight()
        height = img.size[1]
        factor = stdHeight/ float(height)
        rez = ( int(img.size[0]*factor), 
                int(img.size[1]*factor))
        return img.resize(rez, Image.ANTIALIAS)
        
    def find(self, img):
        rImg = img.rotate(180)
        for name in self.bugList:
            print 'comparing to ' + name
            img.save('comp_' + name)
            dbImg = self.bugList[name]
            cmp = Comparison(dbImg, img)
            cmp2 = Comparison(dbImg, rImg)
            print cmp.similarity
            print cmp2.similarity
            threshold = 0.89
            if(cmp.similarity>threshold or cmp2.similarity>threshold):
                print 'match !!'
                sim = cmp.similarity if cmp.similarity>cmp2.similarity else cmp2.similarity
                str0 = 'similarity = ' + str(sim) + ' with image ' + name
                return str0
                
        return 'not in db'
        
def scaleBugImages():

    db = InsectImageDB()
            
    list = []
    cropImgs = []
    
    for (dirpath, dirnames, filenames) in walk(LOAD_BUG_IMG_FOLDER):
        list.extend(filenames)

    for name in filenames:
        iPath = LOAD_BUG_IMG_FOLDER + os.sep + name
        destPath = BUG_DB_FOLDER + os.sep + name
        img1 = Image.open(iPath)
        img2 = FindAndCrop.findAndCropImg(img1)
        stdImg = db.resizeToStandardSize(img2)
        stdImg.save(destPath)
        
        
        