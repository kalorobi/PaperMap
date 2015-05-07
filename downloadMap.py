import urllib, math

class Position:
    """GPS pozicio. lat lon"""
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
 
class Tile:
    """tile"""
    def __init__(self, x, y, zoom):
        self.x = x
        self.y = y
        self.zoom = zoom
        
class DownloadArea:
    """Letoltendo terulet. 
    position1 es position2 pontok altal meghatarozott teglalap
    a letoltendo terulet.
    zoom szukseges a tile meghatarozashoz
    """
        
    def __init__(self, position1, position2, zoom):
        position1XY = self.convertLatLon2XY(position1, zoom)
        position2XY = self.convertLatLon2XY(position2, zoom)
        self.zoom = zoom
        
        if position1XY.x > position2XY.x:
            x = position2XY.x
            self.width = position1XY.x - x + 1
        else:
            x = position1XY.x
            self.width = position2XY.x - x + 1
            
        if position1XY.y > position2XY.y:
            y = position1XY.y
            self.height = position1XY.y - position2XY.y + 1
        else:
            y = position2XY.y
            self.height = position2XY.y - position1XY.y + 1
            
        self.origoXY = Tile(x,y,zoom)
        
    def convertLatLon2XY(self, position, zoom):
        """poziciot tile-re konvertalja """
        lat = math.radians(position.lat)
        n = 2.0 ** zoom
        xtile = int((position.lon + 180.0) / 360.0 * n)
        ytile = int((1.0 - math.log(math.tan(lat) + (1 / math.cos(lat))) / math.pi) / 2.0 * n)
        tile = Tile(xtile, ytile, zoom)
        return (tile)
 
class DownloadMap:
     def __init__(self, map):
         self.map = map
         self.downloadError = False
         
     def downloadTiles(self, dir, downloadArea):
         self.positionXY = Tile(downloadArea.origoXY.x, downloadArea.origoXY.y, downloadArea.origoXY.zoom)
         for x in range(0,downloadArea.width):
             for y in range(0,downloadArea.height):
                 url = self.map + str(self.positionXY.zoom) + '/' + str(self.positionXY.x) + '/' + str(self.positionXY.y) + ".png"
                 file = dir + str(self.positionXY.zoom) + '_' + str(self.positionXY.x) + '_' + str(self.positionXY.y) + ".png"        
                 self.download(url, file)
                 self.positionXY.y = self.positionXY.y - 1
             self.positionXY.x = self.positionXY.x + 1
             self.positionXY.y = downloadArea.origoXY.y
            
     def download(self, url, file):
         try:
             urllib.urlretrieve(url, file)
         except:
            self.downloadError = True
