# 덱
# 큐의 업그레이드 버젼: 선단삽입 or 후단삭제 추가
from CircularQueue import *

class Deck(CircularQueue):      #상속
    def __init__(self):
        super().__init__()      #부모의 생성자는 상속되지x so need super
        
    def addRear(self,item):
        self.enqueue(item)
    
    def deleteFront(self):
        return self.dequeue()   # CQ의 dequeue method에서 isEmpty검사 완료

    def getFront(self):
        return self.peek()

    def addFront(self,item):
        if not self.isFull():
            self.items[self.front]=item
            self.front=((self.front-1)+Max_QSize)%Max_QSize

    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear]    # 다음 연산을 위해 item에 임시저장 return을 바로 주면 종료되어버림
            self.rear=((self.rear-1)+Max_QSize)%Max_QSize
            return item

    def getRear(self):
        if not self.isEmpty():
            return self.items[self.rear]

#TestCode

#deck = Deck()

#deck.addRear(2)
#deck.addFront(1)
#deck.deleteRear()

#deck.display()



            



