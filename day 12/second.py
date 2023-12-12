from functools import cache
from pprint import pprint
list_Req = [] #means how many broken spring i have to add in the sequence
base_State =""
N=0
M=0

# i_bS pos nella stringa

# j_req req da soddisfare 

# brokenS encounter before completing request

# s

@cache
def dp (i_bS, j_req, brokenS ) -> int:
    #pprint((i_bS,j_req,brokenS))
    if j_req==M : 
        j_req=M-1
        brokenS = list_Req[j_req]
    if i_bS == N : return j_req == M-1 and brokenS == list_Req[j_req]
    res = 0
        
    if base_State[i_bS] == "?":
        #can it be a . ? 
        if brokenS ==0: #means we havent started a sequence yet  
            res += dp(i_bS+1,j_req,brokenS)
        
        if brokenS == list_Req[j_req]: # we have endend a sequence
            res+= dp (i_bS+1,j_req+1,0)
        
        #can it be a # 
        if brokenS < list_Req[j_req]:
            res+=dp(i_bS+1,j_req,brokenS+1)
        
    elif base_State[i_bS] == ".":
        if brokenS < list_Req[j_req] and brokenS != 0: #faled branch
            return 0
        if brokenS ==0: #means we havent started a sequence yet  
            res += dp(i_bS+1,j_req,brokenS)
        if brokenS == list_Req[j_req]: # we have endend a sequence
            res+= dp(i_bS+1,j_req+1,0)
    else :
        if brokenS+1>list_Req[j_req]:
            return 0
        res+=dp(i_bS+1,j_req,brokenS+1)
    
    return res    
    
    
with open("day 12/input") as inputFile:
    risp = 0
    allpos=[]
    for sl in inputFile:
        _ = sl.split()
        base_State=_[0].strip()
        base_State+=4*("?"+base_State)
        N = len(base_State)
        list_Req.clear()
        
        for x in _[1].strip().split(","):   
            list_Req.append(int(x))
        lm = list_Req.copy()
        for x in range(4):
            list_Req.extend(lm.copy())
        #pprint(list_Req)
        M =len(list_Req)
        risp+=dp(0,0,0)
        pprint(f"base={base_State},res={risp}, memo = {dp.cache_info() }")
        dp.cache_clear()