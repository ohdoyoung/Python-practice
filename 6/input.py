# print(input())

"""
name = input()
print(name)
print("안녕~", name, "씨 반가워요")

"""

"""
name = input("이름 입력: ")
addr = input("주소 입력: ")
hobby = input("취미 입력: ")

print("안녕~", name, "씨 반가워요")
print("당신은", addr, "에 살고 있군요")
print("당신은", hobby, "를 좋아하는 군요")

"""

# input function practice

"""
print("당신의 고향은 어디인가요? ",end="") -> home = input("당신의 고향은 어디인가요 ? ")
home = input() -> print("아름다운",home,"출신이군요")
print("아름다운",home,"출신이군요")

"""

# question favorite color and animal

color = input("무슨 색을 좋아해요? ")
animal = input("어떤 동물을 좋아해요? ")
print("그럼", color, animal, "를 좋아하겠군요.")  # === print("그럼 %s %s를 좋아하겠군요." % (color,animal))

# question Personal information

name = input("이름이 뭐에요? ")
school = input("당신은 어느 학교를 다니나요? ")
major = input("당신의 전공은 무엇인가요? ")
print(
    name, "씨, 당신은", school, "에서", major, "를 공부하고 있군요"
)  # === print("%s씨, 당신은 %s에서 %s를 공부하고 있군요" % (name,school,major))
