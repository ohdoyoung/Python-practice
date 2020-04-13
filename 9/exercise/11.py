키 = int(input("키가 몇 cm 에요? "))
몸무게 = int(input("몸무게가 몇 kg이에요 "))
미터키 = 키 / 100
bmi = 몸무게 / 미터키 ** 2
print("당신의 BMI: %.2f " % bmi)

if bmi >= 40:
    print("고도비만입니다.")

elif bmi >= 30:
    print("비만입니다.")


elif bmi >= 25:
    print("경도비만입니다.")


elif bmi >= 20:
    print("정상체중입니다.")

else:
    print("저체중입니다.")

