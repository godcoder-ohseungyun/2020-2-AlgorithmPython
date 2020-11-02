class Sort_Set :
    def __init__(self):
        self.items = [] #리스트를 이용하여 집합을 구현

    def isEmpty(self): return len(self.items)==0

    def size(self) : return len(self.items)

    def insert(self,item) :
        if item in self.items : return #이미 존재

        for n in range(len(self.items)): #정렬위치 탐색
            if item < self.items[n]:
                self.items.insert(n,item) #파이썬 리스트 insert연산
                return

        self.items.append(item) #맨후단에 삽이해야하는 경우

    def delete(self,item) :
        if item in self.items : self.items.remove()

    def __eq__(self,setB): # 연산자 중복함수 for 객체 비교
        if self.size() != setB.size() : return False

        for n in range(self.size()):
            if self.items[n] != setB.items [n] : #아닌경우 바로 종료 시킴
                return False
        return True

    def display(self,str="") :
        if not self.isEmpty() :
            print(str)
            for n in range(self.size()):
                print(self.items[n],end=" ")


    def intersect(self,setB) :#교집합 => O(n)
        newSet = Sort_Set()
        a=0
        b=0
        while b< setB.size() and a< self.size() :
            avalue =self.items[a]
            bvalue = setB.items[b]
            if bvalue>avalue:
                a+=1

            if bvalue<avalue:
                b+=1

            if bvalue==avalue: #현재 인덱스가 교집합 이라면 A,B중 하나를 newSet에 삽입
                newSet.items.append(avalue)
                a+=1
                b+=1

        return newSet


    def difference(self,setB) : #차집합 A-B => O(n)
        newSet = Sort_Set()
        a=0
        b=0
        if self == setB : return None #객체 비교후 두 집합이 같으면 공집합 반환
        
        while b< setB.size() and a<self.size() :
            avalue =self.items[a]
            bvalue = setB.items[b]
            if bvalue>avalue:
                newSet.items.append(avalue)
                a+=1

            else: #bvalue가 작거나 두 value가 같은경우 
                b+=1

        while a < self.size(): #나머지 처리
            newSet.items.append(self.items[a])
            a+=1

        return newSet
        

a= Sort_Set()
b= Sort_Set()

a.insert(1)
a.insert(2)
a.insert(3)
a.insert(6)
a.insert(5)

b.insert(3)
b.insert(4)
b.insert(5)

intersect = a.intersect(b)#교집합
difference = a.difference(b)#차집합

a.display("A= ")
print()
b.display("B= ")
print()
intersect.display("교집합: ")
print()
difference.display("차집합: ")
print()


        
