from downloadMap import *
from createMap import *
from paper import *
from downloadTileArea import *

def main():
    
    map = "http://a.tile.openstreetmap.org/"
    poz1 = Position(47.38488, 20.07573)
    poz2 = Position(47.35834, 20.10925)
#    xMin = 9105
#    yMin = 5737
#    xMax = 9107
#    yMax = 5738
    
    zoom = 14
    dir = "/home/tile/"
    dwArea = DownloadArea(poz1,poz2,zoom)  #ha GPS poz alapjan
#    tileArea = DownloadTileArea(xMin, yMin, xMax, yMax, zoom)
#    paper = Paper(poz1, poz2, zoom)        #ha GPS poz alapjan papir meretre
    dwMap = DownloadMap(map)                #terkep letolto
    dwMap.downloadTiles(dir, dwArea)      #letoltes inditas
    
    cm = CreateMap(dir, dwArea)             #terkep osszeallitas

if __name__ == "__main__":
    main()
