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
        print("Map width (XY):%d" %self.widthXY)
        print("Map height (XY:%d" %self.heightXY)
        
        #------------------------------------
        # lapmerethez aranyositas
        #------------------------------------
        dWidthXY, dHeightXY = self.diffCalc(self.widthXY, self.heightXY)
        self.widthXY = self.widthXY + dWidthXY
        self.heightXY = self.heightXY + dHeightXY
        
        print("deltaW: %i, deltaH: %i" %(dWidthXY, dHeightXY))
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
        