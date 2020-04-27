code = input("생년월일 입력:")

y = code[0:4]
print("출생연도: ", code[0:4])
print("생일: ", code[5], "월", code[6:8], "일")
age = 2020 - int(y) + 1
print("나이: ", age, "살")
