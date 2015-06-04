from PIL import Image
from downloadMap import *
from paper import *

#--------------------------------------------
# A letoltott csempeket egyetlen map.png
# keppe allitja ossze.
# dir: letoltott csempek konyvtara
# downloadArea: paper tipus, letoltesi ter.
#--------------------------------------------
class CreateMap:
    
    def __init__(self, dir, downloadArea): #downloadArea -> paper
        positionXY = Tile(downloadArea.origoXY.x, downloadArea.origoXY.y, downloadArea.origoXY.zoom)
        mapWidth = downloadArea.widthXY * 256 #terkep szelesseg pixelben
        mapHeight = downloadArea.heightXY * 256 #terkep magassag pixelben
        map = Image.new("RGB", (mapWidth, mapHeight), "white") #terkep
        
        for x in range(0, downloadArea.widthXY):
            for y in range(0, downloadArea.heightXY):
                file = dir + str(positionXY.zoom) + '_' + str(positionXY.x) + '_' + str(positionXY.y) + ".png"
                tile = Image.open(file)
                map.paste(tile, (x * 256, mapHeight - (y * 256)-256))
                positionXY.y = positionXY.y - 1
            positionXY.x = positionXY.x + 1
            positionXY.y = downloadArea.origoXY.y
        
        #!!!meretre kell vagni PAPER alapjan!!!
        if isinstance(downloadArea, Paper):
            map = map.crop(downloadArea.corpBox)
            print("Map crop")
        map.save(dir + "map.png") #terkep mentes
        print("Created map: %smap.png" %dir)
