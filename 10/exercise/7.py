def scoreinput():
    score = int(input("학점 입력:"))
    return score


def report():
    score = scoreinput()

    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score < 59:
        return "D"


print("나의 성적: ", report())

