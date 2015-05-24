from downloadMap import *
from createMap import *
from paper import *

def main():
    
    map = "http://a.tile.openstreetmap.org/"
    poz1 = Position(47.38488, 20.07573)
    poz2 = Position(47.35834, 20.10925)
    zoom = 15
    dir = "/home/tile/"


    paper = Paper(poz1, poz2, zoom) #papir
#    dwMap = DownloadMap(map)        #terkep letolto
#    dwMap.downloadTiles(dir, paper) #letoltes inditas
    
    cm = CreateMap(dir, paper)      #terkep osszeallitas

if __name__ == "__main__":
    main()
