import sys

n = int(input("정수를 입력하세요: "))

if n <= 0:
    print("양의 정수만 가능합니다. ")
    print("프로그램을 종료합니다. ")
    sys.exit()


if n % 2 == 0:
    print("당신이 입력한 수는 짝수입니다.")
else:
    print("당신이 입력한 수는 홀수입니다.")
