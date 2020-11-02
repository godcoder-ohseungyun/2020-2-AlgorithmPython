#모르스 이진 트리(결정트리)
table = {}

class TNode :
    def __init__(self,data,left,right):
        self.data=data
        self.left=left   #link
        self.right=right #link

def make_morse_tree(): #규칙에 따라 알파벳을 노드 트리로 생성

    root = TNode(None,None,None) # 맨위의 노드는 사용하지 않음 "0값이라 접근연산이 예외적임"
    for tp in table :
       
        code = tp[1] #튜플의 모르스 부분
        node = root

        for c in code :
            if c == '.' :
                if node.left==None:
                    node.left = TNode(None,None,None) #생성
                node = node.left 
            elif c == '-' :
                if node.right == None:
                    node.right = TNode(None,None,None)
                node = node.right 

        node.data = tp[0] #튜플의 알파벳 부분 #노드 트리엔 알파벳만 저장된다.
        
    return root

def encode(ch): #알파벳의 해당하는 모르스 부호를 테이블에서 찾아 반환시키는 함수
    idx = ord(ch)-ord('A')
    return table[idx][1] #튜플 사용법 익혀두기

def decode(root,code) : #code를 사용하기 위해선 따로 list필요함 [테스트코드 참고]
    node = root
    for c in code :
        if c is '.':
            node = node.left
        elif c is '-' :
            node = node.right

    return node.data


#테스트코드

morseCodeTree = make_morse_tree()

str = input("입력하세요 : ")
mlist = []

for ch in str :
    code = encode(ch)
    mlist.append(code)

print("MorseCode: ",mlist)

print("Decoding :",end="")
for code in mlist :
    ch = decode(morseCodeTree,code)
    print(ch,end='')

print()

    



