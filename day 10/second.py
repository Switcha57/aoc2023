
from pprint import pprint
from collections import deque as queue
""" 
The pipes are arranged in a two-dimensional grid of tiles:
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
"""
def find(element, matrix):
    for i, matrix_i in enumerate(matrix):
        for j, value in enumerate(matrix_i):
            if value == element:
                return (i, j)
labirinth=[]

pipe_connections = {
    '|': [(-1, 0),(1, 0)],
    '-': [(0, 1), (0, -1)],
    'L': [(-1, 0),(0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(1, 0),(0, -1)],
    'F': [(1, 0), (0, 1)]
}

with open("day 10/input") as inputFile:
    fl = inputFile.readline().strip()
    labirinth.append(["."]*len(fl)+["."]*2)
    labirinth.append(["."]+[x for x in fl.strip()]+["."])
    for sl in inputFile:
        labirinth.append(["."]+[x for x in sl.strip()]+["."])
    labirinth.append(["."]*len(fl)+["."]*2)
    
#pprint(labirinth)

#need to find S
startPos = find("S",labirinth)

pprint(f"found S {startPos}")

#need to find whiuch symbols is covered by S, only one symbols connect to two adj
#or we can hard code it sample file = F , my input = J
labirinth[startPos[0]][startPos[1]] = 'J'

#distances = [[0]*len(labirinth[0])]*len(labirinth) FAILS
distances = [[0 for col in range(len(labirinth[0]))] for row in range(len(labirinth))]
#time to explore labirinth
pprint(distances)
to_process=[] #curr node, dist, last node
for dirs in pipe_connections[labirinth[startPos[0]][startPos[1]]]:
    to_process.append([(startPos[0]+dirs[0],startPos[1]+dirs[1]),1,(startPos[0],startPos[1])])

while len(to_process)>0: #is not a bfs 
    nw_node = to_process.pop()
    pprint(nw_node)
    if distances[nw_node[0][0]][nw_node[0][1]]==0 or distances[nw_node[0][0]][nw_node[0][1]]>nw_node[1]:
        pprint(f"CHANGING {nw_node[0]}")
        distances[nw_node[0][0]][nw_node[0][1]]=nw_node[1]
        #pprint(distances)
    else:
        continue
    for dirs in pipe_connections[labirinth[nw_node[0][0]][nw_node[0][1]]]:
        pprint(dirs)
        nx = (nw_node[0][0]+dirs[0],nw_node[0][1]+dirs[1])
        if nx!=nw_node[2]:
            pprint(nx)
            to_process.append([nx,nw_node[1]+1,nw_node[0]])

#distances[startPos[0]][startPos[1]]=0


# Second part TW:UGLY
q = queue()
# prepare border
v = 0
#ray cast algorith

for i, matrix_i in enumerate(distances):
    for j, value in enumerate(matrix_i):
        if value ==0:
            labirinth[i][j] = "."
            q.append((i,j))
            #can be a candidate need to check 
while len(q)>0:
    nw_node = q.popleft()
    
    # check number of wall encountered on the left
    leftWall = ["|","J","L"]

    n_lw = 0

    for x in range(nw_node[1]):
        if labirinth[nw_node[0]][x] in leftWall:n_lw+=1

    if n_lw%2:
        v+=1
         
    

with open('out.txt', 'w') as f:
    print(labirinth, file=f)  
pprint(v)
