print("==== 주차료 계산 프로그램 ====")

주차시간 = int(input("주차시간 입력: "))
단위시간 = 주차시간 // 15
요금 = 단위시간 * 1000
print("주차시간: ", 주차시간)
print("주차요금: ", 요금)
