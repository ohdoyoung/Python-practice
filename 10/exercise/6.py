def 높이입력():
    높이 = int(input("높이 입력:"))
    return 높이


def 밑변입력():
    밑변 = int(input("밑변 입력:"))
    return 밑변


def 넓이():
    높이 = 높이입력()
    밑변 = 밑변입력()
    return (밑변 * 높이) / 2


print("삼각형 넓이 : ", 넓이())

