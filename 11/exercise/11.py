import sys

A = int(input("첫 번째 정수 입력:"))
B = int(input("두 번째 정수 입력:"))

if A > B:
    print("A가 더크면 안됨")
    sys.exit()

sum1 = 0

for n in range(A, B + 1, 1):
    sum1 += n

print(sum1)
