# 큐를 이용한 넓이 우선 탐색

from CircularQueue import *
map = [['0','0','0'],
       ['1','0','0'],
       ['0','0','x']]
MAZE_SIZE=3

def isVaild(x,y):
    if x<0 or y<0 or x>MAZE_SIZE or y>MMAZE_SIZE: return False
    return map[x][y]=='0' or map[x][y]=='x'
    

def BFS():
    q=CircularQueue()
    q.enqueue((0,0))

    while not q.isEmpty():
        here=q.dequeue()
        (x,y)=here
        print(here)
        if map[x][y]=='x': return True

        else:
            map[x][y]==',' #지나온 위치는 다른값으로 변경(표시)
            if isValidpos(x,y-1): stack.push((x,y-1))#상
            #구현                                    #하
            #구현                                    #좌
            #구현                                    #우
    return False #출구가 없는 경우
