from pprint import pprint 
#get input and add a buffer
lines=[]
with open("3\input","r") as inputFile:
    for singleline in  inputFile:
        lines.append(singleline)

n_rows = len(lines)+2

schematics=[["."]*(len(lines[0])+1)]
n_cols=len(schematics[0])
for singleline in lines:
    schematics.append(["."]+list(singleline.strip())+["."])
schematics.append(["."]*(len(lines[0])+1))
directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def checkadj(x,y):
    l = []
    for i,j in directions:
        if(schematics[x+i][y+j]=="*"):
            l.append((x+i,y+j))
    return l


pprint(schematics)   
risp=0
gear_found={}
for i in range(1,n_rows):
    curr_num=""
    near_gear=set()
    
    for j in range(1,n_cols):
        #pprint((i,j))
        if(schematics[i][j].isdigit()):
            curr_num+=schematics[i][j]
            l=checkadj(i,j)
            if(len(l)>0):
                near_gear.add(*l)
        else:
            for a in near_gear:
                if a in gear_found:
                    gear_found[a].append(curr_num)
                else:
                    gear_found[a]=[curr_num]
            near_gear.clear()
            curr_num=""
pprint(gear_found)
for ratios in gear_found.values():
    if len(ratios) == 2:
        risp+=(int(ratios[0])*int(ratios[1]))
        
print (risp)