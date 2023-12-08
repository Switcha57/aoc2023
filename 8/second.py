from pprint import pprint
from functools import cache
import sys
import math
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

#AAA ends alway in ZZZ
#MSA ends with XHZ
#PKA end wiith FHZ
#NBA end with LSZ
#RHA end with alw RQZ
#CDA ends with alw LXZ
nodes =["AAA","MSA","PKA","NBA","RHA","CDA"]
calcRisp = []
for node in nodes:
    passi=0
    while(not node.endswith("Z")):
        nxm=moves[passi%N]
        if nxm =="R":
            node=semGraph[node].right
        else:
            node =semGraph[node].left
        passi+=1
    calcRisp.append(passi)

#print(math.prod(calcRisp)/math.gcd(*calcRisp))
print(math.lcm(*calcRisp))