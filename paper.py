from downloadMap import *

#--------------------------------------------
# Papir formatum, a letoltendo teruletet ki-
# egesziti, hogy papir aranyainak megfeleljen
#--------------------------------------------
class Paper(DownloadArea):
    def __init__(self, position1, position2, zoom):
        DownloadArea.__init__(self, position1, position2, zoom)
        print(zoom)
