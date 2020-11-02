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
    hRight = calc_height(node.right)
    if(hLeft>hRight):
        return hLeft+1
    else:
        return hRight+1

#=====================================================================================================
#8.2
def is_complete_binary_tree(root) : #레벨 탐색을 이용한 완전이진트리 판별
    q = queue.Queue()
    q.put(root)
    while not q.empty() :
        n= q.get()
        if n is not None:
            q.put(n.left)
            q.put(n.right)    
        if (not q.empty()) and n==None : #큐에 데이터가 남아있는데 None을 만난경우
            for i in range(q.qsize()):  #남은 데이터중 하나라도 None이 아니라면
                if q.get()!=None :
                    return False    
    return True
#=====================================================================================================
#8.4
def is_balanced(root):
    #calc_height이용 비교
    node=root
    hLeft=calc_height(node.left) #루트의 왼쪽 서브트리의 높이
    hRight=calc_height(node.right) #루트의 오른쪽 서브트리의 높이
    if abs(hLeft-hRight)<2 :  #두수의 차의 절대값이 2 미만
        return True
    return False
    

#=====================================================================================================

#TestCode 8.1-1
def TestCode8_1_1() :
    g = TNode('G',None,None)
    h = TNode('H',None,None)
    d = TNode('D',None,None)
    e = TNode('E',g,h)
    f = TNode('F',None,None)
    b = TNode('B',d,None)
    c = TNode('C',e,f)
    root = TNode('A',b,c)
    print("8.1-1 Tree")

    print('\n In-Order : ' , end='')
    inorder(root)

    print('\n Pre-Order : ' , end='')
    preorder(root)

    print('\n Post-Order : ' , end='')
    postorder(root)

    print('\n Level-Order : ' , end='')
    levelorder(root)

    print()

    print("완전트리인가? : ",is_complete_binary_tree(root))

    print("균형잡혀있는가? : ",is_balanced(root))

    print("==============================================")

#TestCode 8.1-2
def TestCode8_1_2() :
    a=TNode('A',None,None)
    b=TNode('B',None,None)
    slide=TNode('/',a,b)
    c=TNode('C',None,None)
    star2=TNode('*',slide,c)
    d=TNode('D',None,None)
    star1=TNode('*',star2,d)
    e=TNode('E',None,None)
    root=TNode('+',star1,e)
    print("8.1-2 Tree")

    print('\n In-Order : ' , end='')
    inorder(root)

    print('\n Pre-Order : ' , end='')
    preorder(root)

    print('\n Post-Order : ' , end='')
    postorder(root)

    print('\n Level-Order : ' , end='')
    levelorder(root)

    print()

    print("완전트리인가? : ",is_complete_binary_tree(root))

    print("균형잡혀있는가? : ",is_balanced(root))

    print("==============================================")

def TestCode8_2and8_4() :
    c=TNode('C',None,None)
    d=TNode('D',None,None)
    b=TNode('B',c,d)
    f=TNode('F',None,None)
    e=TNode('E',None,f)
    root=TNode('A',b,e)

    print("8.2 and 8.4 Tree")

    print('\n In-Order : ' , end='')
    inorder(root)

    print('\n Pre-Order : ' , end='')
    preorder(root)

    print('\n Post-Order : ' , end='')
    postorder(root)

    print('\n Level-Order : ' , end='')
    levelorder(root)

    print()

    print("완전트리인가? : ",is_complete_binary_tree(root))

    print("균형잡혀있는가? : ",is_balanced(root))

    print("==============================================")

def TestCode8() :
    b=TNode('B',None,None)
    c=TNode('C',None,None)
    root=TNode('A',b,c)

    print("번외: 완전트리인 경우")

    print('\n In-Order : ' , end='')
    inorder(root)

    print('\n Pre-Order : ' , end='')
    preorder(root)

    print('\n Post-Order : ' , end='')
    postorder(root)

    print('\n Level-Order : ' , end='')
    levelorder(root)

    print()

    print("완전트리인가? : ",is_complete_binary_tree(root))

    print("균형잡혀있는가? : ",is_balanced(root))

    print()


#Test

TestCode8_1_1()
TestCode8_1_2()
TestCode8_2and8_4()
TestCode8()
print()