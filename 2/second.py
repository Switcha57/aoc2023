import re



def getN(istt,reg):
    n = 0
    ls = reg.findall(istt)
  #  print(ls)
    
    for nn in ls:
        n+=sum([int(s) for s in nn.split() if s.isdigit()])

    return n

with open("2\input","r") as inputFile:
    wong=0
    r=re.compile("\d{1,2}\sred")
    g=re.compile("\d{1,2}\sgreen")
    b=re.compile("\d{1,2}\sblue")
    for singleline in  inputFile:
        gamestate={
            "red" : 0,
            "green" : 0,
            "blue" : 0,
        }
        nec=[0,0,0]
        #recover game id
        slgame=singleline.split(":")       
        
    
        instances = slgame[1].split(";")
        for ist in instances:
            cur_gs=dict(gamestate)
            cur_gs["green"]-=getN(ist,g)
            cur_gs["blue"]-=getN(ist,b)
            cur_gs["red"]-=getN(ist,r)
            nec=[max(abs(v),nv) for v,nv in zip(cur_gs.values(),nec)]
        #print(nec[0]*nec[1]*nec[2])
        wong+=(nec[0]*nec[1]*nec[2])

print(wong)    
            
        