from prettyprinter import cpprint 
from prettyprinter import pprint 


currMap=[]
 
# transpose so only have to check horizontal symmetrix 

def transpose(m ):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def diffs(l_1, l_2):
    dv = False
    for a, b in zip(l_1, l_2):
        if a != b: 
            dv = True
            break
    return dv

def checkSym(axys, m )->bool:
    print(f"At {axys}" )
    for i in range(min(axys+1,len(m)-axys-1)):

        pprint(f"Checking {axys-i} % {axys+i+1}")
        if (diffs(m[axys-i],m[axys+i+1])):
                return False
        
    
    return True
    
    

def solve(lab) -> int:
    #horizontal symmetry
    rip = 0
    pprint(lab)
    pprint("horizontal ?") 
    for i in range(len(lab)-1):
        #fixed sim axys
        if (checkSym(i,lab)) :
            cpprint(f"found{i}") 
            rip += (i+1) *100
    trm=transpose(lab)
    pprint(trm)
    pprint("veritical ?")
    for i in range(len(trm)-1):
        #fixed sim axys
        if (checkSym(i,trm)) :
            cpprint(f"found{i}") 
            rip += i+1
    return rip

with open("day 13/input","r") as inputFile:
    risp=0
    for sl in inputFile:
        if sl =="\n":
           risp +=solve(currMap)
           currMap.clear()
           continue
        currMap.append([x for x in sl.strip()])
risp +=solve(currMap)
pprint(risp)