

from curses.ascii import isdigit

speeling=["1","2","3","4","5","6","7","8","9","one","two","three","four","five","six","seven","eight","nine"]
dspelt ={
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9",
    
}
risp=0
with open("1\\first\\input","r") as f:
    for sl in f:
        print("e")
        cn=""
        poss=[]
        for tn in speeling:
            p = sl.find(tn)
            if p!=-1: poss.append((p,tn))
            p = sl[::-1].find(tn[::-1])
            if p!=-1: poss.append((len(sl)-1-p,tn))
        poss.sort()
        print(poss)
        if poss[0][1] in dspelt:
            cn+=dspelt[poss[0][1]]
        else:
            cn+=  poss[0][1]
        if poss[-1][1] in dspelt:
            cn+=dspelt[poss[-1][1]]
        else:
            cn+=  poss[-1][1]
              
        risp+=int(cn)
print(risp)    
            