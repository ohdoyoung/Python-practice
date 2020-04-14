print("구구단을 외워보자")
n = int(input("구구단 몇 단을 알려줄까요? "))

for i in range(1, 10, 1):
    print("%d * %d = %d " % (n, i, n * i))

