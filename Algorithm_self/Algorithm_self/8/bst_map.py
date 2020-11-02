#맵은 entry의 집합이다.
#binary tree and binary search tree ADT이용
#이 트리는 크기규칙을 따른다.

from binarytree import *
from binarysearchtree import *

class BSTMap :
    def __init__(self):
        self.root =None

#다양한 메소드
    def isEmpty(self): return self.root==None
    
    def clear(self): self.root=None

    def size(self): return count_node(self.root) #8장 bt

    def search(self,key): return search_bst2(self.root,key) #반복문을 이용한 BST search 이용
    
    def searchValue(self,key): return search_value_vst(self.root,key) #9장 bst

    def findMax(self): return search_max_bst(self.root) #BST MAX 탐색 이용

    def findMIN(self): return search_min_bst(self.root) #BST MIN 탐색 이용
#삽입
    def insert(self,key,value=None):
        node=BSTNode(key,value) #삽입할 노드
        if self.isEmpty() :
            self.root=node
        else :
            insert_bst(self.root,node)
#삭제    
    def delete(self,key) :
        self.root=delete_bst_ALL(self.root,key)
#display
    def display(self,msg='BSTMap: '):#수정필요
        print(msg,end='')
        inorder_bst(self.root) #[중위 탐색] 사용 key값 출력으로 구현
        print()


#TestCode

map = BSTMap()
data=[35,18,7,26,12,3,68,22,30,99] #KEY값 LIST

print("[삽입연산] : ",data)
for key in data:    #삽입
    map.insert(key)
map.display("[중위순회 사용] : ")

if map.search(26) !=None : print("26 탐색성공")
else: print("26 탐색실패")

if map.search(25) !=None : print("25 탐색성공")
else: print("25 탐색실패")

map.delete(3);      map.display("[3 삭제]: ") 
map.delete(68);      map.display("[68 삭제]: ")
map.delete(18);      map.display("[18 삭제]: ")
map.delete(35);      map.display("[35 삭제]: ")
