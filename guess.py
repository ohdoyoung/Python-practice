import random

n = random.randint(1, 99)

while True:
    guess = int(input("1부터 99까지의 정수 중 하나 입력:"))
    if guess > 100:
        print("100이 최대입니다.")
    elif guess > n:
        print("다운")
    elif guess < n:
        print("업")
    else:
        print("정답")
        break
