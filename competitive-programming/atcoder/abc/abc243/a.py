v, a, b, c = map(int, input().split())

while 1:
    if v - a < 0:
        print("F")
        exit()
    v -= a
    if v - b < 0:
        print("M")
        exit()
    v -= b
    if v - c < 0:
        print("T")
        exit()
    v -= c
