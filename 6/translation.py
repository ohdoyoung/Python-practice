import webbrowser

text = input("문장 입력: ")
url = "https://translate.google.co.kr/#ko/en/" + text
webbrowser.open(url)
