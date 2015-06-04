import math
from downloadMap import *

#--------------------------------------------
# Papir formatum, a letoltendo teruletet ki-
# egesziti, hogy papir aranyainak megfeleljen
#--------------------------------------------
class Paper(DownloadArea):
    #szabvanyos oldalarany 1:4142
    
    def __init__(self, position1, position2, zoom):
        DownloadArea.__init__(self, position1, position2, zoom)
        
        # lapmerethez aranyositas
        dWidthXY, dHeightXY = self.diffCalc(self.widthXY, self.heightXY)
        print("Map width (XY): %d + %d" %(self.widthXY, dWidthXY))
        print("Map height (XY):%d + %d" %(self.heightXY, dHeightXY))
        self.widthXY = self.widthXY + dWidthXY
        self.heightXY = self.heightXY + dHeightXY
        
        print("Map origo %d : %d" %(self.origoXY.x, self.origoXY.y))
        #uj origo az eltolas miatt
        self.origoXY = self.origoCalc(self.origoXY, dWidthXY, dHeightXY)
        print("Map new o %d : %d" %(self.origoXY.x, self.origoXY.y))
        
        #kesz terkep vago
        self.corpBox = self.cutMap(self.widthXY, self.heightXY, dWidthXY, dHeightXY)
    #----------------------------------------
    # szabvanyos lapmerethez valo elterest
    # szamol. Szabvany 1:1,4142
    # return: szelesseg es magassag elteres
    #----------------------------------------
    def diffCalc(self, width, height):
        #self.rate = 1.4142
        self.width = width
        self.height = height
        
        rate = float(self.width) / float(self.height)
        
        if rate < 0.708:    #allo nyujtott
            self.width = int(math.ceil(float(self.height) / 1.414 + 0.99))
        elif rate > 0.708 and rate < 1.300: #allo
            self.height = int(math.ceil(float(self.width) * 1.414 + 0.99))
        elif rate > 1.300 and rate < 1.4142: #fekvo
            self.width = int(math.ceil(float(self.height) * 1.414 + 0.99))
        elif rate > 1.4142: #fekvo nyujtott
            self.height = int(math.ceil(float(self.width) / 1.414 + 0.99))
        else:
            print("ERROR")
            
        return (self.width - width, self.height - height)
    #----------------------------------------
    # uj origot szamol, hogy az eredeti te-
    # rulet a lap kozepen legyen
    #----------------------------------------
    def origoCalc(self, origo, dWidth, dHeight):
        if dWidth > dHeight:
            x = int(float(dWhidth) / 2.0)
            x = origo.x - x
            y = origo.y
        else:
            y = int(float(dHeight) / 2.0)
            y = origo.y + y
            x = origo.x
        
        return Tile(x,y, origo.zoom)
    
    def cutMap(self, width, height, dWidth, dHeight):
        print(width * 256, height * 256)
        rate = 1.4142 # papir oldalarany
        w = width * 256  #tile meret
        h = height * 256 #tile meret
        if dWidth > dHeight:
            top = 0
            left = int((float(w) - float(h) / rate) / 2.0)
            w = int(float(h) / rate)
        else:
            top = int((float(h) - float(w) * rate) / 2.0)
            h = int(float(w) * rate)
            left = 0
        
        print("top: %d left: %d w: %d h: %d" %(top, left, w, h))
        return (left, top, w + left, h + top)
        