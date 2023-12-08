from pprint import pprint
from functools import cache
import sys
class dirs:
    left=""
    right=""
    
moves=""
N=0
semGraph ={}

"""@cache
    def dfs(node:str,passi:int) ->int:
    if node=="ZZZ":
        return passi
    nxm=moves[passi]
    #pprint((node,nxm))
    if nxm =="R":
        return dfs(semGraph[node].right,(passi+1)%N)
    else:
        return dfs(semGraph[node].left,(passi+1)%N) """
with open("8/input","r") as inputFile:
    moves=inputFile.readline().strip()
    N=len(moves)
    inputFile.readline()
    for lines in inputFile:
        coord = lines.split("=")
        dd = coord[1].split(",")
        dd[0]=dd[0].strip().removeprefix("(")
        dd[1]=dd[1].strip().removesuffix(")")
        d = dirs()
        d.left=dd[0]
        d.right=dd[1]
        semGraph[coord[0].strip()]=d
        
#print(dfs("AAA",0))
node = "AAA"
passi=0
while(node!="ZZZ"):
    nxm=moves[passi%N]
    if nxm =="R":
        node=semGraph[node].right
    else:
        node =semGraph[node].left
    passi+=1
print(passi)