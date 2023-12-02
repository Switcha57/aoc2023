

from curses.ascii import isdigit


risp=0
with open("1\\first\\input","r") as f:
    for sl in f:
        cn=""
        for c in sl:
            if isdigit(c) :
                cn=cn+c
                break
        for c in sl[::-1]:
            if isdigit(c) :
                cn=cn+c
                break
        risp+=int(cn)
print(risp)    
            