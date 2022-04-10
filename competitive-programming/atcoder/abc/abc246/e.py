# xが縦、yが横
# 下がプラス、右がプラス
from collections import deque
import sys

n = int(sys.stdin.readline())
ax, ay = map(int, sys.stdin.readline().split())
bx, by = map(int, sys.stdin.readline().split())
s = [sys.stdin.readline() for i in range(n)]
ax -= 1
ay -= 1
bx -= 1
by -= 1
INF = 10 ** 9
dp = [[[INF] * 4 for j in range(n)] for i in range(n)]
degree = ((1, 1), (1, -1), (-1, -1), (-1, 1))
q = deque([])

for i in range(4):
    dp[ax][ay][i] = 1
    q.append((ax, ay, i))

while q:
    x, y, d = q.popleft()
    c = dp[x][y][d]

    if x == bx and y == by:
        print(c)
        exit()

    for i in range(4):
        nx = x + degree[i][0]
        ny = y + degree[i][1]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if s[nx][ny] == "#":
            continue

        cost = 0 if d == i else 1
        nc = c + cost

        if dp[nx][ny][i] <= nc:
            continue
        dp[nx][ny][i] = nc

        if cost:
            q.append((nx, ny, i))
        else:
            q.appendleft((nx, ny, i))

print(-1)
