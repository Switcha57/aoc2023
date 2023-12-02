import re



gamestate={
            "red" : 12,
            "green" : 13,
            "blue" : 14,
        }
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
            "red" : 12,
            "green" : 13,
            "blue" : 14,
        }
        #recover game id
        slgame=singleline.split(":")       
        id = int((slgame[0].split(" "))[1])
        wong +=id
        instances = slgame[1].split(";")
        for ist in instances:
            cur_gs=dict(gamestate)
            cur_gs["green"]-=getN(ist,g)
            cur_gs["blue"]-=getN(ist,b)
            cur_gs["red"]-=getN(ist,r)
            if(any([v<0 for v in cur_gs.values()])):
                wong-=id
                break

print(wong)    
            
        