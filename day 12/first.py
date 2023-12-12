from functools import cache
from pprint import pprint
list_Req = [] #means how many broken spring i have to add in the sequence
base_State =""
N=0
M=0

def brute(curr_State : str):
    #print(curr_State)
    if "?" not in curr_State: return [curr_State]
    
    allps = []
    allps.extend(brute(curr_State.replace("?",".",1)))
    allps.extend(brute(curr_State.replace("?","#",1)))
    return allps
    
with open("day 12/input") as inputFile:
    risp = 0
    allpos=[]
    for sl in inputFile:
        _ = sl.split()
        base_State=_[0].strip()
        N = len(base_State)
        list_Req.clear()
        for x in _[1].strip().split(","):   
            list_Req.append(int(x))
        M =len(list_Req) 
        #print(base_State)
        allpos.clear()
        allpos.extend(brute(base_State))
        for possibility in allpos:
            if [len(x) for x in possibility.split(".") if x != ""] == list_Req :
                risp +=1
print(risp)
        