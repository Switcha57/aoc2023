from prettyprinter import cpprint
from prettyprinter import pprint
from collections import deque, namedtuple, defaultdict
import heapq

heatLs = []

Point = namedtuple("Point", "x y")
LEFT, RIGHT, UP, DOWN = Point(0, -1), Point(0, 1), Point(-1, +0), Point(+1, +0)
def direction_to_int(direction: Point):
    if direction == UP: return 0
    if direction == DOWN:  return 1
    if direction == LEFT: return 2
    else: return 3


with open("day 17/input") as fileInput:
    for sl in fileInput:
        heatLs.append([int(x) for x in sl.strip()])


#pprint(heatLs)
N = len(heatLs)
M = len(heatLs[0])
END = Point(N - 1, M - 1)

Node = namedtuple("Node", "heat pos lun dir")


def dijkstra(graph: list[list]):
    global N, M, END, UP, DOWN, RIGHT, LEFT
    # cpprint([UP, DOWN, RIGHT, LEFT])
    pq = []  # type: list[Node]
    # dist = [[[[[-1 for zz in range(3)]for z in range(4)]for x in range(len(graph[0]))]] for _ in range(len(graph))] way to vcomplex to create a four dimentional matrix
    dist = {}
    for i in range(N):
        for j in range(M):
            # for each dir and for each len
            dist[i, j] = [[-1 for x in range(3)] for j in range(4)]
    # cpprint(dist[0,0])
    def is_better(nw_node: Node,cost : int)->bool: 
        cur_best = dist[nw_node.pos.x,nw_node.pos.y][direction_to_int(nw_node.dir)][nw_node.lun]
        
        if cost<cur_best or cur_best ==-1:
            dist[nw_node.pos.x,nw_node.pos.y][direction_to_int(nw_node.dir)][nw_node.lun] =cost
            return True
        
        return False
    heapq.heappush(pq, Node(0, Point(0, 0), 0, DOWN))
    heapq.heappush(pq, Node(0, Point(0, 0), 0, RIGHT))
    pprint(Node(0, Point(0, 0), 0, DOWN))
    pprint(Node(0, Point(0, 0), 0, RIGHT))
    while len(pq) > 0:
        curn = heapq.heappop(pq)
        if curn.pos == END:
            return curn.heat
        for nw_dir in (UP, DOWN, RIGHT, LEFT):
            if nw_dir == curn.dir and curn.lun == 2:
                continue  # not actuyally new dir xd
            if (curn.pos.x + nw_dir.x < 0 or curn.pos.x + nw_dir.x >= N) or (
                    curn.pos.y + nw_dir.y < 0 or curn.pos.y + nw_dir.y >= M
                ): continue
                
            heatLoss = graph[curn.pos.x + nw_dir.x][curn.pos.y + nw_dir.y]
            # check id next pos is better 
            nw_node = Node(0,0,0,0)
            if nw_dir == curn.dir:
                nw_node= Node(-2,Point(curn.pos.x + nw_dir.x,curn.pos.y + nw_dir.y),curn.lun+1,nw_dir)
            else:
                nw_node= Node(-2,Point(curn.pos.x + nw_dir.x,curn.pos.y + nw_dir.y),0,nw_dir)
            if is_better(nw_node,heatLoss+curn.heat):
                nw_node=Node(heatLoss+curn.heat,nw_node.pos,nw_node.lun,nw_node.dir)
                heapq.heappush(pq,nw_node)

                    
    return


cpprint(dijkstra(heatLs)+1)
