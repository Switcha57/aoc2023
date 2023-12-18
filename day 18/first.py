from prettyprinter import pprint
from prettyprinter import cpprint
from collections import namedtuple

Point = namedtuple("Point","x y")

DIRS = "RDLU" 
DIRV = [Point(1,0),Point(0,1),Point(-1,0),Point(0,-1)]

def area(points):
    """"Shoelace formula"""""
    result = 0
    #pprint(type(points))

    for i in range(len(points) -1):
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        result += x1 * y2 - x2*y1

    return abs(result) // 2

with open('day 18/input') as fileInput:
    perimeter = 0
    
    coords_poly = [Point(0, 0)]
    for sl in fileInput:
        dig = sl.split(" ")
        dir =DIRV[DIRS.index(dig[0])]
        lun = int(dig[1])
        perimeter+=lun
        coords_poly.append(Point(coords_poly[-1].x+lun*dir.x,coords_poly[-1].y+lun*dir.y))


    cpprint(area(coords_poly) + perimeter // 2 + 1)