class Entry:
    def __init__(self,key,value):
        self.key = key
        self.value = value

    def __str__(self):
        return str('%s:%s'%(self.key,self.value)) #필요시 문자열로 객체 내역을 변경하여 줌

class LinearProbMap:
    def __init__(self,M):# M:크기
        self.table = [None]*M
        self.M = M

    def hashFn(self,key):#해싱함수
        sum = 0
        for c in key :
            sum = sum+ord(c)

        return sum%self.M

    def insert(self,key,value) :#삽입연산: 루프를 돌다가 빈 공간을 만나면 엔트리 삽입
        idx = self.hashFn(key)
        while True :
            if self.table[idx] == None :  
                self.table[idx]=Entry(key,value) 
                return
            idx=(idx+1)%self.M


    def search(self,key): #탐색연산: 루프를 돌다가 해당하는 table안에서 입력한 키값과 일치하는 데이터를 찾으면 해당 객체 반환
        idx = self.hashFn(key)
        while self.table[idx] :
            if self.table[idx].key == key : 
                return self.table[idx]
            
            idx=(idx+1)%self.M
        return None
        

    def delete(self,key) : #삭제연산: 루프를 돌다가 삭제할 데이터를 찾으면 key,value를 delete,place로 변경하여 삭제됨을 표시
        idx = self.hashFn(key)
        while True :
            if self.table[idx].key == key :
                self.table[idx].key ="delete"
                self.table[idx].value ="place"
                return
            idx=(idx+1)%self.M
       


    def display(self,msg=""):
        print(msg)
        for idx in range(len(self.table)):
            print("[%2d]-> "%idx,self.table[idx])

a=LinearProbMap(10)

a.insert("거북이",200)#삽입
a.insert("고래",80)
a.insert("강아지",18)
a.insert("앵무새",50)
a.insert("침팬치",40)

a.display("동물의 수명")
print()
a.delete("거북이")#삭제
print()
a.display("거북이 삭제->동물의 수명")
print()
print(a.search("고래"))#탐색
print()
print(a.search("코끼리"))#탐색


                








