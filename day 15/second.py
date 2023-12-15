from prettyprinter import pprint

aoc_HashMap = {}

def aoc_Hash (single : str )->int:
    cur_v = 0
    for c in single:
        cur_v+=ord(c)
        cur_v*=17
        cur_v%=256
    return cur_v
        
with open("day 15/input") as fileInput:
    for x in range(256):
        aoc_HashMap[x]=[]
    risp = 0
    to_H = fileInput.readline().split(",")
    for h in to_H:
        if "=" in h:
            bucket,value = h.split("=")
            box = aoc_Hash(bucket)
            for i in range(len(aoc_HashMap[box])):
                if bucket in aoc_HashMap[box][i] :
                    aoc_HashMap[box].pop(i)
                    aoc_HashMap[box].insert(i,bucket+value)                    
                    break;
            else:
                aoc_HashMap[box].append(bucket+value)
        else:
            bucket,value = h.split("-")
            box = aoc_Hash(bucket)
            for i in range(len(aoc_HashMap[box])):
                if bucket in aoc_HashMap[box][i] :
                    aoc_HashMap[box].pop(i)                    
                    break;
            
        #pprint(aoc_HashMap)

risp =0
for box in range(256):
    for slot in range(len(aoc_HashMap[box])):
        risp+= (box+1)*(slot+1)*int(aoc_HashMap[box][slot][-1])

pprint(risp)