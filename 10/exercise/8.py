def numinput():
    num = int(input("정수 입력:"))
    return num


def dist():
    num = numinput()

    if num % 2 == 0:
        print("짝수")
    else:
        print("홀수")


dist()
