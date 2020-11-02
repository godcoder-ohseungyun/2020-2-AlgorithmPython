#=======================================================================================================
#binarysearchtree
#이진 탐색 트리

class BSTNode :
    def __init__(self,key,value) : #엔트리 형식
        self.key=key
        self.value=value
        self.left=None
        self.right=None
#탐색
def search_bst1(node,key): #재귀를 이용한 탐색(key)
    if node == None:
        return None
    if node.key == key :
        return node
    elif node.key>key:
        search_bst(node.left)

    elif node.key<key:
        search_bst(node.right)

def search_bst2(node,key): #반복을 이용한 탐색(key)
  
    while node !=None :
        if node.key == key :
            return node
        elif node.key>key:
            node=node.left
        elif node.key<key:
            node=node.right
    return None

#최대 최소항 탐색
def search_value_bst(node,value): #값을 통한 탐색 O(n) #전체 노드 검사 해야함 #전위탐색 사용

    if node == None : return None
    if node.value is value : return node

    res = search_value_bst(node.left,value)
    if res is not None :
        return res
    else : 
        return search_value_bst(node.right,value)


def search_MAX_bst(node) :
    while node !=None and node.right != None :
        node = node.right
    return node

def search_MIN_bst(node) :
    while node !=None and node.left != None :
        node = node.left
    return node

#삽입
def insert_bst(root,node) : #삽입연산#탐색,순회 이용
    if root.key > node.key:
        if root.left ==None:
            root.left=node
            return True
        else :
            insert_bst(root.left,node)
    elif root.key < node.key :
        if root.right == None:
            root.right=node
            return True
        else :
            insert_bst(root.right,node)
    else:
        return False

def delete_bst_case1 (parent,node,root) : #삭제할 항이 단말노드
    if parent is None:
        root = None
    elif parent.left == node :
        parent.left=None
    elif parent.right ==node :
        parent.right=None
    return root

def delete_bst_case2 (parent,node,root) : #삭제할 항이 자식을 1개 가짐
    if node.left is not None: #이진트리의 모양을 유지하기위해 child가 왼쪽인지 오른쪽인지 구분해야함
        child = node.left
    else:
        child = node.right

    if node is root :
        root = child

    else :
        if parent.left is node :   
            parent.left=child
        else :
            parent.right=child

    return root


def delete_bst_case3 (parent,node,root) : #삭제할 항이 자식을 2개 가짐
    succp = node
    succ = node.right #첫 후계자 후보 (오른쪽 서브트리 이용할것임)
    while succ.left!=None :
        succp=succ
        succ=succ.left
        
    if succp.left is succ :
        succp.left=succ.right

    else :
        succp.right = succ.right

    node.key = succ.key
    node.value = succ.value
    node=succ

    return root

#삭제
def delete_bst_ALL(root,key) : #위 3 case 사용/parent 찾아야함
    if root is None : return None

    parent= None
    node = root

    #탐색이 되거나 탐색이 끝나면 루프 종료
    while node!=None and node.key!=key :
        parent = node
        if node.key>key :
            node=node.left
        else :
            node= node.right
    #결과적으로 parent와 node가 찾아진다.

    if node is None: return None
    if node.left ==None and node.right ==None :
        delete_bst_case1(parent,node,root)
    elif node.left==None or node.right==None:
        delete_bst_case2(parent,node,root)
    else :
        delete_bst_case3(parent,node,root)
    return root

#map구현을 위해 추가 map에서 BSTNode 를 사용함으로 key값을 출력해야함.
def inorder_bst(node) :  #node = root or sub # 1 2 3 중위순회(왼)
    if node is not None :
        inorder_bst(node.left)
        print(node.key,end='  ')
        inorder_bst(node.right)


#=======================================================================================================
#binarytree
#이진트리(노드를 이용하여 구현)
import queue

class TNode :
    def __init__(self,data,left,right):
        self.data=data
        self.left=left   #link
        self.right=right #link


def preorder(node) : #node = root or sub # 2 1 3 전위순회(위)
    if node is not None :
        print(node.data,end='')
        preorder(node.left)
        preorder(node.right)

def inorder(node) :  #node = root or sub # 1 2 3 중위순회(왼)
    if node is not None :
        inorder(node.left)
        print(node.data,end='')
        inorder(node.right)


def postorder(node) :  #node = root or sub # 1 3 2 후위순회(우)
    if node is not None :
        postorder(node.left)
        postorder(node.right) 
        print(node.data,end='')

def levelorder(root) : # 레벨순회: Q이용
    q = queue.Queue()
    q.put(root)
    while not q.empty() :
        n= q.get()
        if n is not None:
            print(n.data,end='')
            q.put(n.left)
            q.put(n.right)

def count_leaf(node) :  #node = root or sub # 노드 개수세기(재귀함수 이용 중요)
    if node is None:
        return 0
    elif node.left is None and node.right is None :
        return 1
    
    else :
        return count_leaf(node.left) + count_leaf(node.right)


def calc_height(node) :  #node = root or sub # 트리의 높이
    if node is None :
        return 0
    hLeft = calc_height(node.left)
    hRight = calc_height(n.right)
    if(hLeft>hRight):
        return hLeft+1
    else:
        return hRight+1

#=======================================================================================================
#BSTMap

#맵은 entry의 집합이다.
#binary tree and binary search tree ADT이용
#이 트리는 크기규칙을 따른다.

#from binarytree import *
#from binarysearchtree import *

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



