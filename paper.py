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
        
        #------------------------------------
        # lapmerethez aranyositas
        #------------------------------------
        dWidthXY, dHeightXY = self.diffCalc(self.widthXY, self.heightXY)
        print("Map width (XY): %d + %d" %(self.widthXY, dWidthXY))
        print("Map height (XY):%d + %d" %(self.heightXY, dHeightXY))
        self.widthXY = self.widthXY + dWidthXY
        self.heightXY = self.heightXY + dHeightXY
        
        print("Map origo %d : %d" %(self.origoXY.x, self.origoXY.y))
        
        self.origoXY = self.origoCalc(self.origoXY, dWidthXY, dHeightXY)
        print("Map new o %d : %d" %(self.origoXY.x, self.origoXY.y))
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
            self.width = int(float(self.height) / 1.414 + 0.99)
        elif rate > 0.708 and rate < 1.300: #allo
            self.height = int(float(self.width) * 1.414 + 0.99)
        elif rate > 1.300 and rate < 1.4142: #fekvo
            self.width = int(float(self.height) * 1.414 + 0.99)
        elif rate > 1.4142: #fekvo nyujtott
            self.height = int(float(self.width) / 1.414 + 0.99)
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
        