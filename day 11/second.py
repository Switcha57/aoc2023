from pprint import pprint
from collections import deque as queue
import bisect

galaxy = []
exp_cols=[]
exp_row = []
EXPS = 1000000

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
    exp_cols.append(col)    
    
    
with open("day 11/input.txt") as inputFile:
    for sl in inputFile:
        singleElements=[x for x in sl.strip()]
        if all([x == "."for x in singleElements]):
            exp_row.append(len(galaxy))
        galaxy.append(singleElements.copy())
for i in range(len(galaxy[0])):
    check_Column(i)

# find coord of every galaxy in not extended galaxy : )
gals = find_Galaxys("#",galaxy)

risp =0

for i in range(len(gals)):
    for j in range(i,len(gals)):
        risp+= (abs(gals[i][0]-gals[j][0]) +abs(gals[i][1]-gals[j][1])
                )+(abs (bisect.bisect_left(exp_row, gals[i][0])-bisect.bisect_left(exp_row, gals[j][0])) +
                   abs (bisect.bisect_left(exp_cols, gals[i][1])-bisect.bisect_left(exp_cols, gals[j][1])))*EXPS-(abs (bisect.bisect_left(exp_row, gals[i][0])-bisect.bisect_left(exp_row, gals[j][0])) +
                   abs (bisect.bisect_left(exp_cols, gals[i][1])-bisect.bisect_left(exp_cols, gals[j][1])))
                

print (risp)