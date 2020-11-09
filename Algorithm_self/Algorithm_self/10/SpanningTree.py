#신장트리


from Stack import *

#쉬운 접근을 위해 딕셔너리 사용

vertex_D = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
vertex = ['A','B','C','D','E','F','G','H']
adjMat = [[0,1,1,0,0,0,0,0],
          [1,0,0,1,0,0,0,0],
          [1,0,0,1,1,0,0,0],
          [0,1,1,0,0,1,0,0],
          [0,0,1,0,0,0,1,1],
          [0,0,0,1,0,0,0,0],
          [0,0,0,0,1,0,0,1],
          [0,0,0,0,1,0,1,0]]
# 신장트리 find
# 책은 인접 리스트 방식이나 인접 행렬 방식으로 풀이
# 무방향 그래프이다.

def bfsST(adj,vertex,start):
    vLen=len(vertex)
    visited = [False]*vLen #for 방문기록
    bfsST_recur(adj,vertex,visited,start)#함수호출

def bfsST_recur(adj,vertex,visited,start):
    
    stack = Stack()
    stack.push(start)       # stack에 시작 좌표 push
    visited.append(start)   # 방문기록

    while stack.top:        #스택이 빌때까지
        col = 0             #열
        v=stack.pop() 
        
        for n in adj[vertex_D[v]]:  #딕셔너리를 이용해 '키'의 value에 해당하는 adj 행을 검사
            if n==1 and (not vertex[col] in visited): # 값이 1이고 방분한적이 없을때
               print("(",v,",",vertex[col],")")       # 출력(행문자,열문자)
               stack.push(vertex[col])                # 방문한 열 스택에 삽입
               visited.append(vertex[col])            # 방문기록 저장 
               
            col+=1                                    # 열 +1


#TestCode
bfsST(adjMat,vertex,'A')
