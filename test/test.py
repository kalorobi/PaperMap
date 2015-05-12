from downloadMap import *

def main():
    poz1 = Position(47.38488, 20.07573)
    poz2 = Position(47.35834, 20.10925)
    zoom = 15
    
    dw = DownloadArea(poz1, poz2, zoom)
    
    print("X:%d Y:%d" %(dw.origoXY.x, dw.origoXY.y))
    print("w:%d h:%d" %(dw.width, dw.height))
    map = "http://a.tile.openstreetmap.org/"
    dir = "/home/tile/"
    dt = DownloadMap(map)
    dt.downloadTiles(dir, dw)
   
main()
