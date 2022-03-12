# スライド最小値による解法
import sys
from collections import deque

w, n = map(int, sys.stdin.readline().split())
INF = -float("inf")
dp = [[INF for j in range(w + 1)] for i in range(n + 1)]
dp[0][0] = 0
slider = deque([])


def solve(i, j, slider: deque):
    s = j - R
    g = j - L
    if g < 0:
        dp[i][j] = dp[i - 1][j]
        return

    while slider and slider[0] < s:
        slider.popleft()
    while slider and dp[i - 1][slider[-1]] < dp[i - 1][g]:
        slider.pop()
    slider.append(g)

    dp[i][j] = max(dp[i - 1][j], dp[i - 1][slider[0]] + dish)


for i in range(1, n + 1):
    L, R, dish = map(int, sys.stdin.readline().split())
    for j in range(w + 1):
        solve(i, j, slider)
    while slider:
        slider.pop()


ans = dp[n][w]

if ans == INF:
    print(-1)
else:
    print(ans)
