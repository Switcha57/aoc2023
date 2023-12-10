from pprint import pprint

def maps(sources: list,inp):
    arrivals=[]
    inp.readline()
    for line in inp:
        if line =="\n": break
        toRem=[]
        (detR,sorR,lenR)=[int(v) for v in  line.split(" ")]    
        for v in sources:
            if v>=sorR and v<sorR+lenR:
                arrivals.append(detR+(v-sorR))
                toRem.append(v)
        sources[:]=[x for x in sources if not (x in toRem)]
    for x in sources:
        arrivals.append(x)
    return arrivals

with open("5/input","r") as inputFile:
    getSeed= [int(v) for v in (inputFile.readline().split(":"))[1].strip().split(" ")]
    (inputFile.readline())
    for i in range(0,7):
        getSeed=maps(getSeed,inputFile)
        pprint(getSeed)
        
    print (min(getSeed))
