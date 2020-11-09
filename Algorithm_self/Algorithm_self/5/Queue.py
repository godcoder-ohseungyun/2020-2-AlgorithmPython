#일반 큐
class Queue:
    def __init__(self):
        self.items= []

    def isEmpty(self):
        return len(self.items)==0

    def size(self):
        return len(self.items)

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)


# 라이브러리에서 제공한다.
# import queue
# q=queue.Queue() #() 안에 크기 지정  default==무한
# put get empty full size
# 주의: put get 함수를 사용할때 언더플로 or 오버플로가 발생하는데 error출력 x 무한루프 o 이다 
# 따라서 사용전에 full과 empty로 상태 check필수!

