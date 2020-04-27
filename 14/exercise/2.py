import sys

str1 = input("입력: ")
length = len(str1.encode("utf-8"))

acount = str1.count("a") + str1.count("A")
ocount = str1.count("o") + str1.count("O")

print("전체문자 개수: ", length, "글자")
print("문자 A 개수: ", acount, "개")
print("문자 O 개수: ", ocount, "개")
