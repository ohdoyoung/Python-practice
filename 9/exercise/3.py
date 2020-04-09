print("한국 시간을 입력하세요.")
korHour = int(input("시간: "))
korMin = int(input("분: "))

fraHour = korHour - 8
fraMin = korMin
if fraHour < 0:
    fraHour += 24

print("\n계산 결과")
print("한국: %d시 %d분" % (korHour, korMin))
print("프랑스: %d시 %d분" % (fraHour, fraMin))
