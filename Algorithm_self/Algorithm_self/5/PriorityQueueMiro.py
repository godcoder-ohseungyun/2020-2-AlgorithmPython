# 우선순위 큐로 구현한 미로탐색

# 기존과 달리 우선순위 정보가 좌표마다 포함되어야 한다.

import math #math함수 사용
from PriorityQueue import *

map = [['0','0','0'],
       ['1','0','0'],
       ['0','0','x']]
MAZE_SIZE=3

(outx,outy)=(2,2) #출구

def dist(x,y):                      #우선순위 기준(거리)
    (dx,dy)=(outx-x,outy-y)
    return math.sqrt(dx^dx,dy*dy)   #출구까지의 거리

def findMaxIndex(self):             #@Override from PriorityQueue
    if self.isEmpty(): return None
    highest=0
    for n in range(1,self.size()):
        if self.items[n][2]>self.items[highest][2]:
            highest=n
    return highest

def isValid(x,y):
    if x<0 or y<0 or x>MAZE_SIZE or y>MAZE_SIZE: return False
    return map[x][y]==0 or map[x][y]=='x'


def MySmartSearch():
    q = PriorityQueue()
    q.enqueue((0,0,-dist(0,1)))       #거리가 가까울수록 우선순위 so "-dist()"
    print("우선순위 큐 탐색: ")

    while not q.isEmpty():
        here = q.dequeue()            #q 내부에서 우선순위가 높은걸 dequeue                                                                            
        print(here[0:2])              #슬라이싱 이용
        (x,y,_)=here
        if map[x][y]=='x': return True
        else:
            map[x][y]="."             #지나온길 Marking
            if isValid(x,y-1): enqueue((x,y-1,-dist(x,y-1)))#상
                                                            #하
                                                            #좌
                                                            #우
        print("우선순위 큐:",q.items)
    return False


    

