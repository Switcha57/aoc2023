from pprint import pprint
from collections import deque as queue

galaxy = []
to_add=[]


def find_Galaxys(element, matrix):
    gals = []
    for i, matrix_i in enumerate(matrix):
        for j, value in enumerate(matrix_i):
            if value == element:
                gals.append( (i, j))
    return gals


def check_Column(col):
    for x in range(len(galaxy)):
        if galaxy[x][col] == "#":
            return
    to_add.append(col)    
    
    
with open("day 11/input.txt") as inputFile:
    for sl in inputFile:
        singleElements=[x for x in sl.strip()]
        if all([x == "."for x in singleElements]):
            galaxy.append(singleElements.copy())
        galaxy.append(singleElements.copy())
for i in range(len(galaxy[0])):
    check_Column(i)

while len(to_add)>0:
    c = to_add.pop()
    for x in range(len(galaxy)):
        galaxy[x].insert(c,".")


# find coord of every galaxy in extended galaxy
gals = find_Galaxys("#",galaxy)

risp =0

for i in range(len(gals)):
    for j in range(i,len(gals)):
        risp+= abs(gals[i][0]-gals[j][0]) +abs(gals[i][1]-gals[j][1])  

print (risp)