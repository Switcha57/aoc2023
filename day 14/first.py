from prettyprinter import cpprint
from prettyprinter import pprint


game = []

def drop(coords,boulders):
    i,j = coords
    
    while i>0 and boulders[i-1][j] == ".":
        i-=1
        continue
    boulders[coords[0]][coords[1]]= "."
    boulders[i][coords[1]]= "O"
     

def drop_north(mine):
    for j in range(1,len(mine)):
        for k in range(len(mine)):
            if (mine[j][k] =='O'):
                drop((j,k),mine)

with open("day 14/input") as fileInput:
    for sl in fileInput:
        game.append([x for x in sl.strip()])
        
drop_north(game)        
#cpprint(game)
risp = 0
for i in range(len(game)):
    for j in game[i]:
        if j == "O":
            risp += (len(game)-i)

pprint(risp)