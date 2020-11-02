#class
class Polynomial :
    def __init__(self): #생성자
        self.coef = []
        

    def degree(self) :  #차수반환
        return len(self.coef)-1

    def eval(self,scalar) :       #evaluate
        result = 0
        for n in range(len(self.coef),0,-1) : 
            result += self.coef[n-1]*(scalar**(n-1))
        return result

    # + 
    def add(self,rhs) :   
        p = Polynomial()
        value = len(self.coef) if len(self.coef)>=len(rhs.coef) else len(rhs.coef) #삼항연산 이용 value는 두 다항식 중 차수가 큰값을 도출
        if(len(self.coef)== value) :
            rhs.coef.extend([0]*(value-len(rhs.coef)))                             #리스트는 동적 배열임을 이용.
        if(len(rhs.coef)== value) :                                                #작은 다항식은 차만큼 list에 '0'을 확장
            self.coef.extend([0]*(value-len(self.coef)))  
        for n in range(value) :                                                    #두 배열의 크기가 같아졌기때문에 value만큼 범위를 벗어나지않고 루프 완전히 돌수있음.
            p.coef.append(self.coef[n] + rhs.coef[n])
        return p
    # -     
    def subtract(self,rhs) : 
        p = Polynomial()
        value = len(self.coef) if len(self.coef)>=len(rhs.coef) else len(rhs.coef) # add모듈과 주석 동일

        if(value == len(self.coef)) :
            rhs.coef.extend([0]*(value-len(rhs.coef)))            

        if(value == len(rhs.coef)) :                                                
            self.coef.extend([0]*(value-len(self.coef)))          
        
        for n in range(value) :                                                     
             p.coef.append( self.coef[n]- rhs.coef[n] )

        return p   
    # *              
    def multiply(self,rhs) : # 다중 반복문을 이용한 다항식 곱연산.
        p = Polynomial()
        getArray = [0]*(len(self.coef)+len(rhs.coef)-1) #임시 list생성 크기는 증가 차수 만큼
        for n in range(len(self.coef)): #다중 for문 
            for m in range(len(rhs.coef)): 
                 getArray[n+m] += rhs.coef[m]*self.coef[n] #해당하는 차수에 수가 대입될수있도록 한다.
        p.coef = getArray
        return p
 
       
    def display(self,str) : #개선 완료 (불필요 중복 제거,0값은 생략)
        print(str,end = " ")
        for n in range((len(self.coef)),0,-1) :        
            if((n-1)!=0) :   #차수항             
                if(self.coef[n-1]!=0) :
                    print(self.coef[n-1],"x^",n-1,end=" ")
                    if(self.coef[n-2]>0) : #다음 차수의 계수가 양수이면 미리 +추가
                        print("+",end=" ")               
                if(self.coef[n-1]==0) :
                    print(end=" ")
            if((n-1)==0) :  #상수항
                if(self.coef[n-1]!=0) :
                    print(self.coef[n-1])               
                if(self.coef[n-1]==0) :
                    print() #마지막 상수가 0일때는 개행문자를 포함하여야 한다.


def read_poly() :#스플릿 이용 한줄로 입력 가능
    p = Polynomial()
   
    deg = int(input("다항식의 최고 차수를 입력하시오: "))
    print("다항식의 계수를 차례로 입력하세요.: ",end =" ")
    p.coef = list(map(float,input().split())) #split 문자열 나누기->형변환->list화
    p.coef.reverse()    
    return p

#testcode
if __name__ == "__main__" : #이 파일 직접실행된 모듈일때만 실행되도록.
    a = read_poly()
    b = read_poly()
    c = a.add(b)
    d = a.subtract(b)
    f = a.multiply(b)
    a.display("A(x) = ")
    b.display("B(x) = ")
    c.display("C(x):다항식의 합 = ")
    d.display("D(x):다항식의 차 = ")
    f.display("F(x):다항식의 곱 = ")
    print( " C(2) = ",c.eval(2))