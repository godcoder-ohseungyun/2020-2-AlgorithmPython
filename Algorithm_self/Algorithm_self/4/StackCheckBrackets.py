# 스택을 활용한 괄호검사

# 조건 1: 왼쪽과 오른쪽 괄호의 개수가 같아야한다.
# 조건 2: 같은 타입의 괄호에서 왼쪽이 오른쪽보다 먼저 나와야한다.
# 조건 3: 서로 다른 타입의 괄호 한쌍이 교차하면 안된다.

# 파일은 라인별로 읽어들여 리스트에 저장한다.

# 파이썬에서 ' " 둘다 문자열을 나타내며 기능 차이는 x
from Stack import *

def checkBrackets(lines) :
    stack = Stack()

    for line in lines:
        for c in line:
            if c in "{[(" :
                stack.push(c)
            else :
                if stack.isEmpty(): return False # 조건 2
                left = stack.pop() # \ 로 줄바꿔쓰기 가능
                if left == "{" and c !="}" or \
                left=="[" and c !="]" or \
                left=="(" and c != ")" : return False  #조건 3
        
        return stack.isEmpty() #조건 1

def isValidSource(lines):
    stack = Stack()
    eCode = 0   #에러 코드
    Icnt = 0    #라인위치
    ccnt = 0    #문자 위치

    case1 = False # ' ' 안에 들어있는경우
    case2 = False # " " 안에 들어있는경우

    for line in lines:
        
        Icnt+=1 #라인 증가
        
        for c in line:
            ccnt +=1
            if c == '#': continue # break 이나 ccnt를 세기위해 continue로 변경
             #원래 이후 검사 필요x 다음라인으로 go //break:해당 반목문 전체 종료
 
            if c == "'": 
                if case1 : case1 = False #다시 ' 를 만났을때 case가 켜져있는경우 off
                else : case1 = True #처음 ' 를 만났을때 case on 하고 하위 무시
                continue

            if c == '"': 
                if case1 : case1 = False
                else : case1 = True
                continue        # continue:현재 루프의 맨 밑으로 이동 //continue아래 문장들 skip

            if case1 or case2 : continue # case인경우 계속 하위 skip

            if c in "{[(" :
                stack.push(c)
            else :
                if c in "}])":
                    if stack.isEmpty(): return "조건 2 위반",Icnt,ccnt  # 조건 2 
                    else:
                        left = stack.pop() 
                        if (left != "{" and c =="}") or \
                        (left !="[" and c =="]") or \
                        (left !="(" and c == ")") : return "조건 3 위반",Icnt,ccnt  #조건 3
 
        
    if not stack.isEmpty() : return "조건 1 위반",Icnt,ccnt  #검사 종료후 스텍이 비어있지 않으면 조건 1 위반
    else : return "오류없음",0,0

#파일처리 코드
filename = "C:/Users/user/Desktop/CheckBracketMain.cpp"
infile = open(filename,"r")#읽기모드
lines = infile.readlines()
infile.close()

eCode,Icnt,ccnt = isValidSource(lines) #반환값 여러개를 가질수 있다.
print(filename," ----> ",eCode)
print("라인 위치: " ,Icnt)
print("문자 위치: ",ccnt)