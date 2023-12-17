from prettyprinter import pprint
from prettyprinter import cpprint
from collections import deque
mirrorGrid=[]

with open("day 16/input") as fileInput:
    for sl in fileInput:
        mirrorGrid.append([x for x in sl.strip()])

m, n = len(mirrorGrid), len(mirrorGrid[0])
visited = set()
energized = set()
Q = deque([(0, 0, 'right')])   
while Q:
    x, y, direction = Q.pop()
    energized.add((x, y))
    tile = mirrorGrid[x][y]

    if y < n-1 and (x, y+1, 'right') not in visited and (
            (direction == 'right' and tile in '.-') or 
            (direction == 'up' and tile in '/-') or
            (direction == 'down' and tile in '\\-')):
        Q.append((x, y+1, 'right'))
        visited.add((x, y+1, 'right'))

    if x > 0 and (x-1, y, 'up') not in visited and (
            (direction == 'up' and tile in '.|') or 
            (direction == 'right' and tile in '/|') or
            (direction == 'left' and tile in '\\|')):
        Q.append((x-1, y, 'up'))
        visited.add((x-1, y, 'up'))

    if y > 0 and (x, y-1, 'left') not in visited and (
            (direction == 'left' and tile in '.-') or 
            (direction == 'up' and tile in '\\-') or
            (direction == 'down' and tile in '/-')):
        Q.append((x, y-1, 'left'))
        visited.add((x, y-1, 'left'))

    if x < m-1 and (x+1, y, 'down') not in visited and (
            (direction == 'down' and tile in '.|') or 
            (direction == 'right' and tile in '\\|') or
            (direction == 'left' and tile in '/|')):
        Q.append((x+1, y, 'down'))     
        visited.add((x+1, y, 'down'))

cpprint(len(energized))