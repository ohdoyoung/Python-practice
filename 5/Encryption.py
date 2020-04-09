# 암호화 하기

letter = "Hello Python"
encodeLetter = ""

for ch in letter:
    num = ord(ch)
    encodeLetter += chr(num + 1)

print("원문 : ", letter)
print("암호 : ", encodeLetter)

# 해석 하기

decodeLetter = ""
for ch in encodeLetter:
    num = ord(ch)
    decodeLetter += chr(num - 1)

print("암호 해제: ", decodeLetter)

