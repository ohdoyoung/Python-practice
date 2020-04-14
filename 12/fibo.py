"""
(Pseudo Code) <- 재귀

def fibo(n):
    if n==1 or n==2:
        return 1
    else :
        return fibo(n-1) + fibo(n-2)

    while 1:
        n = int(input("피보나치 N: "))
        fb=fibo(n)
        print("피보나치(%d) : %d"%(n,fb))

"""

## 수학적 방식

import math

while 1:
    n = int(input("양의 정수 N: "))
    result1 = 1 / math.sqrt(5) * math.pow((1 + math.sqrt(5)) / 2, n)
    result2 = 1 / math.sqrt(5) * math.pow((1 - math.sqrt(5)) / 2, n)
    result = result1 - result2
    print("답은: %d " % result)

