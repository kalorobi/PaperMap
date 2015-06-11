import math
from downloadMap import *

class DownloadTileArea(DownloadArea):
    def __init__(self, xMin, yMin, xMax, yMax, zoom):
        lat, lon = self.convertXY2LatLon(xMin, yMin, zoom)
        position1 = Position(lat, lon)
        lat, lon = self.convertXY2LatLon(xMax, yMax, zoom)
        position2 = Position(lat, lon)
        DownloadArea.__init__(self, position1, position2, zoom)
        
        print("position1 -> lat:%f - lon:%f" %(position1.lat, position1.lon))
        print("position2 -> lat:%f - lon:%f" %(position2.lat, position2.lon))
    #----------------------------------------
    # pozicio szamitas tile alapjan WIKI
    #----------------------------------------
    def convertXY2LatLon(self, x, y, zoom):
        n = 2.0 ** zoom
        lon_deg = x / n * 360.0 - 180.0
        lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * y / n)))
        lat_deg = math.degrees(lat_rad)
        return (lat_deg, lon_deg)