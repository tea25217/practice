from math import floor


x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

d = floor((((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5) * 10 ** 6)
diffR = floor(abs(r1 - r2) * 10 ** 6)
sumR = floor((r1 + r2) * 10 ** 6)


if d < diffR:
    print(1)
elif d == diffR:
    print(2)
elif d == sumR:
    print(4)
elif d > sumR:
    print(5)
else:
    print(3)
