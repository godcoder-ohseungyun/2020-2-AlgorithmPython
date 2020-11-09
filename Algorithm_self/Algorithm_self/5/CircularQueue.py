# 원형 큐
# 주의 front와 rear을 기준으로 사용함으로 메소드도 이에 맞춰 구성

Max_QSize=10

class CircularQueue:
    def __init__(self):
        self.front=0
        self.rear=0
        self.items=[None]*Max_QSize #None 꼭 써줘야함

    def isEmpty(self):
        return self.front==self.rear
    def isFull(self):           #제한된 리스트이기때문에 필요함
        return self.front==(self.rear+1)%Max_QSize

    def clear(self):
        self.front=self.rear

    def enqueue(self,item):
        if not self.isFull():   #검사 필수
            self.rear=(self.rear+1)%Max_QSize
            self.items[self.rear]=item


    def dequeue(self):
        if not isEmpty():       #검사 필수
            self.front=(self.front+1)%Max_QSize
            return self.items[self.front]  #원형 큐에선 굳이 삭제pop 필요 x

    def peek(self):
        if not isEmpty():
            return self.items[(self.front+1)%Max_QSize]

    def size(self):
        return (self.rear-self.front+Max_QSize)%Max_QSize   #흐음...

    def display(self):                                      #두개의 경우의수
        out=[]
        if self.front<self.rear:
            out=self.items[self.front+1:self.rear+1]
        else :
            out=self.items[(self.front+1)%Max_QSize:0]\
               +self.items[0:self.rear+1]
        print("f: ",self.front,"r: ",self.rear,"==> ",out)


#TestCode
#q = CircularQueue()

#q.enqueue(1)
#q.enqueue(1)
#q.enqueue(1)
#q.enqueue(1)
#q.display()




