#=============================================================================
class Node :    #노드
    def __init__(self,data,link=None):
        self.data = data
        self.link = link
#=============================================================================
class Linked_List:  #연결된 리스트
    def __init__(self):
        self.head=None

    def isEmpty(self) : return self.head == None

    def clear(self) : self.head = None

    def size(self) : 
        node = self.head
        count = 0
        while not node == None :
            node = node.link
            count+=1
        return count

    def display(self,msg="Linked List") :
        print(msg,end='')
        node=self.head
        while not node == None :
             print(node.data,end='')
             node = node.link
        print()


    def getNode(self,pos): #해당 위치의 노드 반환
        if pos == None: return None
        node =  self.head
        while pos > 0 and node != None:
            node = node.link #다음 노드로 이동
            pos -= 1
        return node


    def insert(self,pos,data): #해당 위치에 노드 삽입
        before = self.getNode(pos-1)
        if before == None: self.head = Node(data,self.head)
        else:
            node = Node(data,before.link)
            before.link = node

    def delete(self,pos):   #해당 위치의 노드 삭제
        before = self.getNode(pos-1)
        if before == None: 
            if self.head != None: self.head = self.head.link

        elif before.link != None:
            before.link=before.link.link
#=============================================================================
class Term :    #노드의 데이터 부분에 삽입될 데이터 class
    def __init__(self,expon,coeff):
        self.expon = expon #차수
        self.coeff = coeff #계수
#=============================================================================
class Sparse_Polynomial(Linked_List):   #상속
    def __init__(self):
        super().__init__()  #부모클래스 생성자 호출

    def degree(self): #최고차항 반환
        if self.head == None: return 0
        elif self.head !=None: return self.head.data.expon 

    def display(self,msg=""): #디스플레이
        print(msg,end='')
        node=self.head
        while  node :
            if node.data.coeff != 0: #계수가 0일땐 출력하지 x
               
                if node.data.expon != 0: #상수항이 아닐때

                    if node == self.head :#첫번째 항 출력일때
                        print(node.data.coeff," X^",node.data.expon," ",end='')

                    elif node != self.head :#첫번째 항 출력이 아닐때

                        if node.data.coeff < 0 :  #계수 음수일때
                            print(node.data.coeff," X^",node.data.expon," ",end='')
                        if node.data.coeff > 0 :  #계수 양수일때 +기호 추가
                            print(" + ",node.data.coeff," X^",node.data.expon," ",end='')

                elif node.data.expon == 0 : #상수항일때
                    if node.data.coeff < 0 :  #계수 음수일때
                           print(node.data.coeff,end='')
                    if node.data.coeff > 0 :  #계수 양수일때 +기호 추가
                           print(" + ",node.data.coeff,end='')
            node = node.link
        print()
       
    
    def read(self): #입력
        self.clear()
        token = input("계수 차수 계수 차수...[엔터]").split(" ") #" "(공백) 기준으로 나누어 리스트에 저장
        for i in range(len(token)//2) : # // 소수점 이하는 버림 연산자
            self.insert(self.size(),Term(int(token[i*2+1]),float(token[i*2]))) #차수 계수 순으로 저장 노드를 데이터로 전송

    def add(self,B): #+
        p = Sparse_Polynomial()
        aN = self.head
        BN = B.head

        while aN and BN  : #노드가 있는한 반복 #None이 아닌 값은 true를 가짐을 인지
            if aN.data.expon == BN.data.expon : # 차수가 같은경우 
                sum = aN.data.coeff + BN.data.coeff
                p.insert(p.size(),Term(aN.data.expon,sum)) #노드 삽입
                aN = aN.link    #다음 노드
                BN = BN.link    #다음 노드

            elif aN.data.expon > BN.data.expon :# a차수가 큰 경우
                p.insert(p.size(),Term(aN.data.expon,aN.data.coeff))
                aN = aN.link #다음 노드

            elif aN.data.expon < BN.data.expon :# B차수가 큰 경우
                 p.insert(p.size(),Term(BN.data.expon,BN.data.coeff))
                 BN = BN.link #다음 노드
            

        #둘중 하나가 None이 되면 루프 탈출 임으로 남은 노드는 별도로 수행
        while aN :  #BN이 None이고 aN의 노드가 남아있을때
            p.insert(p.size(),Term(aN.data.expon,aN.data.coeff))
            aN = aN.link    #다음 노드
        while BN :  #aN이 None이고 BN의 노드가 남아있을때
            p.insert(p.size(),Term(BN.data.expon,BN.data.coeff))
            BN = BN.link    #다음 노드

        return p

    def __neg__(self): # -Object 정의 @오버라이딩
        p = Sparse_Polynomial()
        node = self.head
        while node :
            p.insert(p.size(),Term(node.data.expon,-(node.data.coeff)))
            node = node.link
        return p

    def sub(self,B): #-
        return self.add(-B)


    def mult(self, B) :       
        selfNode = self.head    
        BNode = B.head      
        temp = Sparse_Polynomial()  #임시로 노드를 받아둘 객체
        result = Sparse_Polynomial()  #결과 노드를 받을 객체
        while selfNode : #노드가 없을때까지 반복
            while BNode :
                temp.insert(temp.size(), Term(selfNode.data.expon + BNode.data.expon,  selfNode.data.coeff * BNode.data.coeff))    #임시 객체에 노드 생성
                BNode = BNode.link       
            result = result.add(temp)  #곱해진 결과를 결과에 더해줌  
            selfNode = selfNode.link     
            temp.clear()  #다음 루프에서 저장을 위해 temp clear()               
            BNode = B.head               
        return result #최종 결과
#=============================================================================


a = Sparse_Polynomial()
b = Sparse_Polynomial()
a.read()
b.read()
a.display(" A = ")
b.display(" B = ")
c = a.add(b)
c.display("C = ")
d = a.sub(b)
d.display("D = ")
e = a.mult(b)
e.display("E = ")
