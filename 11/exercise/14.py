sum1 = 0
for n in range(50, 101, 1):
    if n % 3 == 0:
        sum1 += n
    elif n % 5 == 0:
        sum1 += n

print(sum1)

