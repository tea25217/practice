from math import atan2, pi, sin


T = int(input())
L, X, Y = map(int, input().split())
q = int(input())
L /= 2


def solver(e):
    t = e % T
    tRad = (t / T) * 2 * pi
    x0 = 0
    y0 = L * -sin(tRad)
    z0 = L * sin(tRad - pi / 2) + L

    dist = ((X - x0) ** 2 + (Y - y0) ** 2) ** 0.5

    return atan2(z0, dist) * 180 / pi


for i in range(q):
    e = int(input())
    print(solver(e))
