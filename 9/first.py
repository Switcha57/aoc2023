


#trying naive solve

def get_lower(q):
    ret=[]
    for i in range(1,len(q)):
        ret.append(q[i]-q[i-1])
    return ret
#* placeHolder
def missing_link(query):
    if not any(query):
        return 0
    nq =  get_lower(query)
    return query[-1]+missing_link(nq)
    
risp = 0
with open("9/input") as inputFile:
    for single in inputFile:
        query = [int(x) for x in single.split()]
        risp+=missing_link(query)
    #    query.append("*")
print (risp)