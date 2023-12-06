import re

n = 0
def f (x):
    return (n-x)*x
#find the maximum of the function so we can divide in one crescent and one decreasing so we can bs that value
def ternary_search(l, r) :
    eps = 3;              #set the error limit here
    while (r - l > eps) :
        m1 = l + (r - l) // 3;
        m2 = r - (r - l) // 3;
        f1 = f(m1);      #evaluates the function at m1
        f2 = f(m2);      #evaluates the function at m2
        if (f1 < f2):
            l = m1;
        else:
            r = m2;
    curr_max = (l,f(l))
    l+=1
    while l<=r:
        if(f(l)>curr_max[1]):
            curr_max=(l,f(l))
        l+=1
    return curr_max                    #return the maximum of f(x) in [l, r]

with open("6/input","r") as inputFile:
  #  numbs = re.compile("\b\d{1,3}\b")
    ist = inputFile.readline().split(":")[1].strip()
    nList=[int(s) for s in ist.split() if s.isdigit()]
    ist = inputFile.readline().split(":")[1]
    disList=[int(s) for s in ist.split() if s.isdigit()]
    risp = 1
    for t in range(len(nList)):
        n = nList[t]
        #print(ternary_search(0,t))
        maxDist = ternary_search(0,n)
        print(maxDist)
        if maxDist[1] > disList[t]:
            #function increasing till maxdist[0] then decreasing
            l = -1
            r = maxDist[0]
            while (r - l > 1) :
                m = (l + r) // 2;
                if (f(m)>disList[t]) :
                    r = m #// 0 = f(l) < f(m) = 1
                else :
                    l = m #// 0 = f(m) < f(r) = 1  
            startWin = l+1
            l = maxDist[0]
            r = n
            while (r - l > 1) :
                m = (l + r) // 2;
                if (f(m)<=disList[t]) :
                    r = m #// 0 = f(l) < f(m) = 1
                else :
                    l = m #// 0 = f(m) < f(r) = 1  
            beforeLoss = l
            risp*=(beforeLoss-startWin+1)
            
        print(risp)