# 우선순위 큐
# 정렬 되어 있지 않는게 특징

from Queue import *

class PriorityQueue(Queue):
    def __init__(self):
        super().__init__()    #책은 따로 정의했지만 상속을 이용하자.

    def findMaxIndex(self): #가장 높은 인덱스 위치를 알아야함
        if not self.isEmpty():
            highest=0
            for n in range(1,self.size()):
                if self.items[n]>self.items[highest] :
                    highest=n
            return highest
  
        return None

    def dequeue(self):
        if not self.isEmpty():
            highest=self.findMaxIndex()
            if highest is not None:             #검사 필요
                return self.items.pop(highest)  #해당 인덱스 pop

#TestCode

p = PriorityQueue()

p.enqueue(1)
p.enqueue(5)
p.enqueue(4)
p.enqueue(3)

print(p.dequeue())

