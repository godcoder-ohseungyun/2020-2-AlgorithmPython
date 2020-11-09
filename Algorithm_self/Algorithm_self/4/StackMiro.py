#스택을 이용한 미로탐색

from Stack import *

map = [['0','0','0'],
       ['1','0','0'],
       ['0','0','x']]
MAZE_SIZE=3

def isValidpos(x,y):
    if x<0 or y<0 or x>=MAZE_SIZE or y>=MAZE_SIZE : return False

    else: return map[x][y]=='x' or map[x][y]=='0' #여기 중요 boolean 응용

def DFS(): #깊이 우선탐색
    stack = Stack()
    stack.push((0,0))   #튜플로 시작위치 스택 삽입
    print("DFS: ")

    while not isEmpty():
        here=stack.pop() #현위치

        (x,y)=here #튜플을 받아올수잇음 !! (중요)

        if map[x][y]=='x': return True
        else:
            map[x][y]==',' #지나온 위치는 다른값으로 변경(표시)!!

            if isValidpos(x,y-1): stack.push((x,y-1))#상
            #구현                                    #하
            #구현                                    #좌
            #구현                                    #우
        print(stack.top)
    
    return False #출구가 없는 경우