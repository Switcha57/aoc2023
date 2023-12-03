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
    
    return any([(not schematics[x+i][y+j].isdigit())and((schematics[x+i][y+j]!=".")) for i,j in directions ]) 


pprint(schematics)   
risp=0
for i in range(1,n_rows):
    curr_num=""
    adjPart = False
    
    for j in range(1,n_cols):
        #pprint((i,j))
        if(schematics[i][j].isdigit()):
            curr_num+=schematics[i][j]
            if not adjPart:
                adjPart=checkadj(i,j)
        else:
            if(adjPart):
                risp+=int(curr_num)
            adjPart=False
            curr_num=""
print (risp)