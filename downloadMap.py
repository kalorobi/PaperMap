#============================================
# downloadMap.py    V0.1    2015.05.21.     =
#                                           =
# Terkep csempeket megadott konyvtarba tolt =
#-------------------------------------------=
# haznalat:                                 =
# map = "http://a.tile.openstreetmap.org/"  =
# poz1 = Position(47.38488, 20.07573)       =
# poz2 = Position(47.35834, 20.10925)       =
# zoom = 15                                 =
# dir = "/home/tile/"                       =
# dwArea = DownloadArea(poz1, poz2, zoom)   =
# dwMap = DownloadMap(map)                  =
# dwMap.DownloadTiles(dir, dwArea)          =
#============================================

import math
import urllib

#--------------------------------------------
# GPS pozicio.
# lat: float tipusu
# lon: float tipusu
#--------------------------------------------
class Position:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

#--------------------------------------------
# Tile (csempe) leirasara valo osztaly.
# x,y: tile "pozicioja"
# zoom: a terkepen a zoom szint.
#--------------------------------------------
class Tile:
    def __init__(self, x, y, zoom):
        self.x = x
        self.y = y
        self.zoom = zoom

#--------------------------------------------
# Letoletendo terulet, melyet egyertelmuen
# meghataroz a position1 es position2.
# position1 es postion2: Position tipusu.
# zoom: a tile meghatarozashoz szukseges.
#
# widthXY, heightXY: szamitott ertekek, a
# letoltendo terulet szelessege es magassaga
# csempe szamban.
#
# origoXY: a letoltendo terulet origoja, bal
# also sarok, csempe pozicio.
#--------------------------------------------
class DownloadArea:
    def __init__(self, position1, position2, zoom):
        position1XY = self.convertLatLon2XY(position1, zoom)
        position2XY = self.convertLatLon2XY(position2, zoom)
        self.zoom = zoom
        
        if position1XY.x > position2XY.x:
            x = position2XY.x
            self.widthXY = position1XY.x - x + 1
        else:
            x = position1XY.x
            self.widthXY = position2XY.x - x + 1
            
        if position1XY.y > position2XY.y:
            y = position1XY.y
            self.heightXY = position1XY.y - position2XY.y + 1
        else:
            y = position2XY.y
            self.heightXY = position2XY.y - position1XY.y + 1
            
        self.origoXY = Tile(x, y, zoom)
    #----------------------------------------
    # poziciot szamit at tile poziciora. WIKI
    #----------------------------------------
    def convertLatLon2XY(self, position, zoom):
        """poziciot tile-re konvertalja """
        lat = math.radians(position.lat)
        n = 2.0 ** zoom
        xtile = int((position.lon + 180.0) / 360.0 * n)
        ytile = int((1.0 - math.log(math.tan(lat) + (1 / math.cos(lat))) / math.pi) / 2.0 * n)
        tile = Tile(xtile, ytile, zoom)
        return (tile)

#--------------------------------------------
# Terkep letoltes. 
# map: pl.:http://a.tile.openstreetmap.com/
#
# downloadTiles() osztaly vegzi a letoltest.
# dir: string, csempe mentes helye
# downloadArea: DownloadArea tipus, letoltendo
#--------------------------------------------
class DownloadMap:
    def __init__(self, map):
        self.map = map
        self.downloadError = False #letoltes kozbeni hiba
        self.wrongTiles = [] #hibas csempek
         
    def downloadTiles(self, dir, downloadArea):
        positionXY = Tile(downloadArea.origoXY.x, downloadArea.origoXY.y, downloadArea.origoXY.zoom)
        print("download tiles: %s" % str(downloadArea.widthXY * downloadArea.heightXY))
         
        for x in range(0, downloadArea.widthXY):
            for y in range(0, downloadArea.heightXY):
                url = self.map + str(positionXY.zoom) + '/' + str(positionXY.x) + '/' + str(positionXY.y) + ".png"
                file = dir + str(positionXY.zoom) + '_' + str(positionXY.x) + '_' + str(positionXY.y) + ".png"
                self.download(url, file) #tile letoltes
                positionXY.y = positionXY.y - 1
            positionXY.x = positionXY.x + 1
            positionXY.y = downloadArea.origoXY.y
        
        if self.downloadError != True: #hiba ellenorzes
            print("Downloading completed!")
        else:
            print("---E R R O R---") #ide kell a hiba kezeles
            for wrong in self.wrongTiles:
                print("wrong tile: %s" % wrong)
                
    #----------------------------------------
    # csempe letoltes es kozvetlen mentes
    #----------------------------------------
    def download(self, url, file):
        try:
            urllib.urlretrieve(url, file)
            print("download:%s ->OK" %url)
        except:
            self.downloadError = True
            self.wrongTiles.append(url)
            print("download:%s ->ERROR" %url)
            