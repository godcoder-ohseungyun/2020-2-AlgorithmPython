# 스택
# 후입선출
# 되돌리기 기능,재귀함수(함수호출루프),괄호검사,계산기

class Stack :
    def __init__(self):
        self.top=[]

    def isEmpty(self):
        return len(self.top)==0

    def size(self):
        return len(self.top)

    def clear(self):
       self.top=[]

    def push(self,item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty() : #비어있는지 검사 필수
            return self.top.pop(-1) # List[-n] // 뒤에서 n번째 위치 컨텍

    def peek(self):
        if not isEmpty():
            return self.top[-1]

    def display(self):
        print(self.top)
       
#TestCode

#stack = Stack()

#stack.push("나는")
#stack.push("멋진")
#stack.push("코더")
#stack.push("이다")
#stack.display()
#stack.pop()
#stack.display()