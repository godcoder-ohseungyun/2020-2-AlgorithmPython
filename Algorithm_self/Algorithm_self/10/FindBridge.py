#삭제시 연결이 끊어지는 브릿지 찾기
from Stack import *


vertex = ['A','B','C','D','E','F','G','H']
adjMat = [[0,1,1,0,0,0,0,0],
          [1,0,0,1,0,0,0,0],
          [1,0,0,1,1,0,0,0],
          [0,1,1,0,0,1,0,0],
          [0,0,1,0,0,0,1,1],
          [0,0,0,1,0,0,0,0],
          [0,0,0,0,1,0,0,1],
          [0,0,0,0,1,0,1,0]]

def find_bridges(adj,vertex):
    stack=Stack()   #스택이용
    v= len(vertex)  #루플을 돌릴 횟수
    for i in range(v):
        count=0
        for j in range(v):
            if adj[i][j]==1 : #순차적으로 루프를 돌리다가 1값을 만나면 count and push(j)
                count+=1
                stack.push(j)
        if count==1:          #만약 해당 라인에 1값이 단 한개라면 브릿지
            print("(",vertex[i],",",vertex[stack.pop()],")")    #stack 최상단에 있는 j 값 출력

#TestCode

find_bridges(adjMat,vertex)

 

    
