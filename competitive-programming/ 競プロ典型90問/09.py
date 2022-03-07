from bisect import bisect_left
from math import atan2, pi


n = int(input())
dots = [""] * n
for i in range(n):
    x, y = map(int, input().split())
    dots[i] = (x, y)
dots.sort()
ans = 0


def getAngle(origin, dot):
    x, y = dot[0], dot[1]
    x -= origin[0]
    y -= origin[1]
    return atan2(y, x) * 180 / pi


def solve(dot):
    angleList = [getAngle(dot, i) for i in dots if dot != i]
    angleList.sort()
    ans = 0
    for a in angleList:
        opposite = (a + 180) % 360
        idx = bisect_left(angleList, opposite)
        idx2 = idx - 1
        if idx == 0:
            idx2 = len(angleList) - 1
        elif idx == len(angleList):
            idx = 0
        if abs(opposite - angleList[idx]) < abs(opposite - angleList[idx2]):
            c = angleList[idx]
        else:
            c = angleList[idx2]
        angle = min(abs(a - c), 360 - abs(a - c))
        ans = max(ans, angle)
    return ans


for i in dots:
    ans = max(ans, solve(i))

print(ans)
