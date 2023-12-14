from prettyprinter import cpprint
from prettyprinter import pprint
import time
import copy
game = []

def shift_v(rows, direction):
    if direction == "N":
        row_order = range(len(rows))
    else:
        row_order = range(len(rows) - 1, -1, -1)

    for column_index in range(len(rows[0])):
        empty = []

        for row_index in row_order:
            match rows[row_index][column_index]:
                case ".":
                    empty.append(row_index)
                case "#":
                    empty = []
                case "O":
                    if empty:
                        rows[empty.pop(0)][column_index] = "O"
                        rows[row_index][column_index] = "."
                        empty.append(row_index)


def shift_h(rows, direction):
    if direction == "E":
        column_order = range(len(rows[0]) - 1, -1, -1)
    else:
        column_order = range(len(rows[0]))

    for row_index in range(len(rows)):
        empty = []

        for column_index in column_order:
            match rows[row_index][column_index]:
                case ".":
                    empty.append(column_index)
                case "#":
                    empty = []
                case "O":
                    if empty:
                        rows[row_index][empty.pop(0)] = "O"
                        rows[row_index][column_index] = "."
                        empty.append(column_index)


def calc_risp(game):
    risp = 0
    for i in range(len(game)):
        for j in game[i]:
            if j == "O":
                risp += (len(game)-i)
    return risp

with open("day 14/input") as fileInput:
    for sl in fileInput:
        game.append([x for x in sl.strip()])
        
       
#cpprint(game)
# pprint(game)
def spin():
    shift_v(game, "N")
    shift_h(game, "W")
    shift_v(game, "S")
    shift_h(game, "E")
    
    # pprint(game)
    
ciclo=[]
spin()

print(calc_risp(game))
while game not in ciclo:
    
    ciclo.append(copy.deepcopy(game))
    spin()
    # cpprint(game)    
    #pprint(calc_risp(game))
    #time.sleep(0.5)

start_loop=ciclo.index(game)
loop_len = len(ciclo) - start_loop
#print(loop_len)
#print(start_loop)
#print(calc_risp(game))

for i in range(((1_000_000_000 -start_loop)%loop_len)-1):
    spin()

print(calc_risp(game))
