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

