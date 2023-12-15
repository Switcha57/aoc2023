

def aoc_Hash (single : str )->int:
    cur_v = 0
    for c in single:
        cur_v+=ord(c)
        cur_v*=17
        cur_v%=256
    return cur_v
        
with open("day 15/input") as fileInput:
    risp = 0
    to_H = fileInput.readline().split(",")
    for h in to_H:
        risp += aoc_Hash(h)
    print(risp)