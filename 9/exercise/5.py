import sys

num = int(input("정수 입력: "))

if num <= 0:
    print("양의 정수만 가능합니다. ")
    print("프로그램을 종료합니다. ")
    sys.exit()

if num % 3 == 0:
    print("3의 배수")
else:
    print("3의 배수 아님")
