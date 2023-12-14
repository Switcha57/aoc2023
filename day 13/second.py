from prettyprinter import cpprint 
from prettyprinter import pprint 


currMap=[]
 
# transpose so only have to check horizontal symmetrix 

def transpose(m ):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def diffs(l_1, l_2):
    dv = 0
    for a, b in zip(l_1, l_2):
        if a != b: 
            dv += 1
            
    return dv
d =0
def checkSym(axys, m )->bool:
    print(f"At {axys}" )
    global d
    for i in range(min(axys+1,len(m)-axys-1)):

        pprint(f"Checking {axys-i} % {axys+i+1}")
        d+=diffs(m[axys-i],m[axys+i+1])
        if d> 1:
            return False 
    else:
        if d == 1:
            return True
        
        
    
    return False
    
    

def solve(lab) -> int:
    #horizontal symmetry
    rip = 0
    global d
    pprint(lab)
    pprint("horizontal ?") 
    for i in range(len(lab)-1):
        d  =0
        #fixed sim axys
        if (checkSym(i,lab)) :
            cpprint(f"found{i}") 
            rip += (i+1) *100
            break
    
    trm=transpose(lab)
    pprint(trm)
    pprint("veritical ?")
    for i in range(len(trm)-1):
        d  =0
        #fixed sim axys
        if (checkSym(i,trm)) :
            cpprint(f"found{i}") 
            rip += i+1
            break
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