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
    