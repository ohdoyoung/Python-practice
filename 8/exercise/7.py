"""
print("=== 원리금 계산 프로그램 ===")
money = int(input("저축금액 입력:"))
print("원금: %d" % money)
이자 = float(money) / (3.75 / 100)
print("이자: %d" % 이자)
세금 = 이자 / (15 / 100)
print("세금: %d" % 세금)
print("최종: %d" % money + 이자 + 세금)
"""
