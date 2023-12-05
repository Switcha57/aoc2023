from pprint import pprint


def overlapping_segment(start1, length1, start2, length2):
    end1 = start1 + length1
    end2 = start2 + length2
    if max(start1, start2) < min(end1, end2):  # Check if there is an overlap
        overlap_start = max(start1, start2)
        overlap_end = min(end1, end2)
        overlap_length = overlap_end - overlap_start
        return (overlap_start, overlap_length)
    return None 
# check if two range overlap

def maps(sources: list,inp):
    arrivals=[]
    inp.readline()
    for line in inp:
        if line =="\n": break
        toRedo=[]
        (detR,sorR,lenR)=[int(v) for v in  line.split(" ")]    
        while len(sources)>0:
            v=sources.pop()
            newR = overlapping_segment(v[0],v[1],sorR,lenR)
            if newR is not None:
                arrivals.append((detR+newR[0]-sorR,newR[1]))
                #create new sx segment and dx segment
                if newR[0]>v[0]: 
                    toRedo.append((v[0],newR[0]-v[0]))
                
                if(newR[0]+newR[1]<v[0]+v[1]):
                    toRedo.append((newR[0]+newR[1],v[0]+v[1]-(newR[0]+newR[1])))
            else:
                toRedo.append(v)
        sources[:]=[v for v in toRedo]
             
        
    for x in sources:
        arrivals.append(x)
    return arrivals

with open("5/input","r") as inputFile:
    getSeed= [int(v) for v in (inputFile.readline().split(":"))[1].strip().split(" ")]
    (inputFile.readline())
    TgetSeed=[]
    for i in range(0,len(getSeed),2):
        TgetSeed.append((getSeed[i],getSeed[i+1]))
    for i in range(0,7):
        TgetSeed=maps(TgetSeed,inputFile)
        pprint(TgetSeed)
        
    print (min(TgetSeed)[0])
