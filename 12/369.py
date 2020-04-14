import time

print("369게임 시작")
n = 1
while n <= 20:
    if n % 3 == 0 or "3" in str(n):
        print("박수")
    else:
        print(n)
    n += 1
    time.sleep(0.7)

print("369게임끝")
