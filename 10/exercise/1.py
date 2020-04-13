def Nameinput():
    name = input("이름 입력:")
    return name


def Homeinput():
    home = input("고향 입력:")
    return home


def profile():
    name = Nameinput()
    home = Homeinput()
    print("이름:", name)
    print("고향:", home)


profile()
