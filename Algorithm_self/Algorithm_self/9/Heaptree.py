
#힙 트리(무조건 완전 이진 트리)

#비교후 큰쪽으로 이동한다.
#기존 이진트리를 규칙에 따라 정리한 트리
# 최대힙=내림차순 | 최소힙=오름차순

class MaxHeap :
    def __init__(self) :
        self.heap = []
        self.heap.append(0) #0번지 항목 미리 추가(사용 안함)

    def size(self) : return len(self.heap)-1 #0번지 제외 -1
    def isEmpty() : return self.size() is 0 
    def Parent(self,i) : return self.heap[i//2]
    def Left(self,i) : return self.heap[i*2]
    def Right(self,i) : return self.heap[i*2+1]
    def display(self,msg="힙트리 : ") :
        print(msg,self.heap[1:])    #슬라이싱 이용

#삽입연산
    def insert(self,node) :
        self.heap.append(node)
        i = self.size()

        while (i != 1 and node > self.Parent(i)) :  #업힙 이라면
            self.heap[i] = self.Parent(i)   #새 노드 위치에 부모를 삽입
            i = i//2    #부모 위치 

        self.heap[i] = node #부모위치에 새 노드 삽입(업 힙)

#삭제연산 (루트를 삭제하는것)
    def delete(self) :
        parent=1 #첫 부모 위치 in Heap
        child=2  #첫 자식 위치 in Heap

        if not self.isEmpty() :
            hroot = self.heap[1]
            last = self.heap[self.size()] #마지막 노드를 사용할것임
            while (child <= self.size()) :
                if child<self.size() and  self.Left[parent] < self.Right[parent] :#오른쪽이 더 큰경우
                    child +=1
                elif last > self.heap[child] :  #이동이 필요없는경우
                    break
                self.heap[parent]=self.heap[child]
                parent=child
                child *= 2
        self.heap[parent]=last
        self.heap.pop(-1)
        return hroot


#test code
heap = MaxHeap()

data = [2,5,4,8,9,3,7,3]

for elem in data:
    heap.insert(elem)

heap.display()

heap.delete()

heap.display()


   