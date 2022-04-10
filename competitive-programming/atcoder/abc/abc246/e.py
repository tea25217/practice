# xが縦、yが横
# 下がプラス、右がプラス
from collections import deque
import sys
sys.setrecursionlimit(1000000000)

n = int(sys.stdin.readline())
ax, ay = map(int, sys.stdin.readline().split())
bx, by = map(int, sys.stdin.readline().split())
s = [sys.stdin.readline() for i in range(n)]
ax -= 1
ay -= 1
bx -= 1
by -= 1
INF = 10 ** 9
dp = [[INF] * n for _ in range(n)]
degree = ((1, 1), (1, -1), (-1, -1), (-1, 1))

q = deque([])
for d in degree:
    if ax + d[0] < 0 or ax + d[0] >= n or ay + d[1] < 0 or ay + d[1] >= n:
        continue
    q.append((ax, ay, d, 1))

while q:
    x, y, d, c = q.pop()

    if x == bx and y == by:
        break

    for nd in degree:
        nx = x + nd[0]
        ny = y + nd[1]

        if x + nx < 0 or x + nx >= n or y + ny < 0 or y + ny >= n:
            continue
        if s[nx][ny] == "#":
            continue

        if d != nd:
            nc = c + 1
        else:
            nc = c

        if dp[nx][ny] <= nc:
            continue
        dp[nx][ny] = nc

        if d == nd:
            q.appendleft((nx, ny, nd, nc))
        else:
            q.append((nx, ny, nd, nc))

if dp[bx][by] == INF:
    print(-1)
else:
    print(d[bx][by])
