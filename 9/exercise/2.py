from datetime import date

today = date.today()

birthYear = int(input("몇 년도에 태어났나요? "))
age = today.year - birthYear + 1

print("올해 당신은 %d살입니다." % age)

if age >= 15 and age < 20:
    print("당신은 청소년입니다.")
elif age >= 20:
    print("당신은 성인입니다.")
