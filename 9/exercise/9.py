from datetime import date

today = date.today()

birthYear = int(input("몇 년도에 태어났나요? "))
age = today.year - birthYear + 1

if age <= 7:
    print("어린이 입니다.")

elif age <= 13:
    print("초등학생 입니다.")

elif age <= 16:
    print("중학생 입니다.")

elif age <= 19:
    print("고등학생 입니다.")

elif age <= 26:
    print("대학생 입니다.")

elif age >= 27:
    print("직장인 입니다.")
