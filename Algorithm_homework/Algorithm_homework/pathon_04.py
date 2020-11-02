class Stack :
    def __init__(self):
        self.top = [] #list

    def isEmpty(self) : return len(self.top)==0 #using boolean type

    def size(self) : return len(self.top)

    def clear(self) : self.top = [] #make list empty

    def push(self,item) : #스텍에 삽입
        self.top.append(item)

    def pop(self) :  #스텍상단 pop
        if not self.isEmpty() : 
            return self.top.pop(-1)

    def peak(self) :
        if not self.isEmpty() : return self.top[-1] # return reverse arrangement no."-1"

def isValidSource(lines) : #checking for parenthesis correctness 
    stack = Stack() #Stack's object
    line_c = 0 
    for line in lines :# lines: 파일의 각 줄을 문자열 인자로 같는 list
        line_c += 1 # counting variable to find error line
        word_c = 0  # counting variable to find error word
        for chr in line : # in read documents
            word_c += 1 
            if chr in "{([" :
                if chr not in "'{''(''['" :#조건추가
                    stack.push(chr)
            elif chr in "})]" :
                if chr not in "'}'')'']'" :#조건추가
                    if stack.isEmpty() :
                        return "조건 2 위반",line_c,word_c
                    else :
                        leftch = stack.pop()
                        if (chr == "}" and leftch != "{") or \
                           (chr == "]" and leftch !="[") or  \
                           (chr == ")" and leftch != "(") :
                            return "조건 3 위반",line_c,word_c
    if stack.isEmpty() : #using boolean type
        return "문제 없음",0,0
    else :
        return "조건 1 위반",line_c,word_c
 

filename = input("검사를 실시할 파일 이름을 입력하시오. :")
infile = open(filename,"r")
lines = infile.readlines(); # Read line by line and save String type
infile.close()

eCode, lcnt, ccnt = isValidSource(lines) # 3 returns
print(filename, " ---> ", eCode)
print(" 라인수 = ", lcnt)
print(" 문자수 = ", ccnt)
