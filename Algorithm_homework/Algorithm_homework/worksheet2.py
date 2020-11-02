import time # for using time method

#Fibonacci (순환)
def fib(n) :
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return fib(n-1) + fib(n-2)

#Fibonacci (반복)
def fib_iter(n) :
    if(n<2) :
        return n

    last = 0
    current =1
    for i in range(2,n+1) : # return 2 ~ n 
        tmp = current
        current += last
        last = tmp
    return current 

#===============================================================

t1 = time.time() # save time

print('반복')
for i in range (1,40) :
    print(str(fib_iter(i)),end=' ') #str() change number type to string , Removing newline characters(end='')

t2 = time.time() # save time

print(' ')
print('runtime',t2-t1)

print('순환')

t1 = time.time() 

for i in range (1,40) :
    print(fib(i))

t2 = time.time()

print('runtime',t2-t1)
