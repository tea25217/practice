from math import cos, pi, sin


a, b, h, m = map(int, input().split())

ax = a * cos((30 * h + 0.5 * m) * pi / 180)
ay = a * sin((30 * h + 0.5 * m) * pi / 180)
bx = b * cos(6 * m * pi / 180)
by = b * sin(6 * m * pi / 180)

ans = (abs(ax - bx) ** 2 + abs(ay - by) ** 2) ** 0.5

print(ans)
