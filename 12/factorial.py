def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


print("팩토리얼 값 계산 프로그램")
while 1:
    n = int(input("\n입력 : "))
    if n <= 0:
        break
    result = factorial(n)
    print("%d! = %d" % (n, result))
