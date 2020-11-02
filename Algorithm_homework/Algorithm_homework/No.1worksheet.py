
# Bag (리스트 메소드 이용)
# 함수 def , 들여쓰기 부분이 함수 영역({} 사용 x)

def contain(bag,e) :
    return e in bag # if e in bag[], return true else false

def insert(bag,e) :
    bag.append(e)  #insert method , append() is a Python list method
    
def remove(bag,e) :
    bag.remove(e)  #remove method , remove() is a Python list method

def count(bag) :
    return len(bag) # count method


def numOf(bag, e) :
    count = 0
    for i in range(len(bag)) :#range(A) method to return 0 ~ (A-1) for Iteration 
        if bag[i] == e : 
            count = count + 1
    return count


#==========================================================

myBag =[]                      # The empty list for Bag

insert(myBag, '휴대폰')        # insert cell phone in Bag
insert(myBag, '지갑')          # insert wallet in Bag
insert(myBag, '손수건')        # insert handkerchief in Bag
insert(myBag, '빗')           # insert comb in Bag
insert(myBag, '자료구조')      # insert data structure in Bag
insert(myBag, '야구공')        # insert baseball in Bag

print('list in bag', myBag)    # print list

insert(myBag,'빗')            # insert comb again in Bag
remove(myBag, '손수건')        # remove handkerchief in Bag

print('list in bag', myBag)    # print list

print('number of comb',numOf(myBag, '빗')) # return number of comb
print('number of wallet',numOf(myBag, '지갑')) # return number of wallet