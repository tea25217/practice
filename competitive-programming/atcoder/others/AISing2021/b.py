s = input()[::-1].translate(str.maketrans({'6': '9', '9': '6'}))
print(s)
