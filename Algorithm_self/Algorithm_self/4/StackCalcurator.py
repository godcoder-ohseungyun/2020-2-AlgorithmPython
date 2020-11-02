#스택을 이용한 계산기

#사용자는 중위표기법으로 입력 변환후 컴퓨터는 후위표기법으로 연산처리
#후위표기법 연산 및 중위표기법->후위표기법 변환 기능
from Stack import *

#후위표기 연산
def evalPostfix(expr):
    stack = Stack()

    for token in expr:
        if token in "+-*/":
            v1=stack.pop() 
            v2=stack.pop()
            if token=="+": stack.push(v2+v1) #나중에 나오는 수가 첫 수
            if token=="-": stack.push(v2-v1)
            if token=="/": stack.push(v2/v1)
            if token=="*": stack.push(v2*v1)

        else :
            stack.push(token)

    return stack.pop() #최종 스택의 수가 답

#중위표기->후위표기 변환

def precedence(op): #우선순위 메소드 
    if op=='(' or op==')': return 0 #괄호를 가장 우선순위 낮게 설정
    if op=='+' or op=='-': return 1
    if op=='*' or op=='/': return 2
    else: return -1

def Infix2postfix(expr):
    s = Stack()
    output = [] #출력 리스트

    for term in expr:
        if term in "(":
            s.push(term)
        elif term in ")":
            while not isEmpty():
                op=s.pop()
                if op=="(":break
                else: output.append(op)

        elif term in "+-/*":
            while not isEmpty():
                op = s.peek()
                if (precedence(term)<=precedence(op)): #우선순위 검사후 바로->list 인지 -> Stack인지 판별 
                    output.append(op)
                    s.pop()
                else:
                    break
            s.push(term)

        else:
            output.append(term) #피연산자는 바로 -> list

    while not isEmpty():
        output.append(s.pop())

    return output
                    
               


