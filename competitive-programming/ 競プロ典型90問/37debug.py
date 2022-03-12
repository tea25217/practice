# 愚直解と比較するデバッグコード
# 誤：dequeからpopleftする条件が<=
# 正：<

from random import randint
from collections import deque


def debug():
    dp = [[INF for j in range(w + 1)] for i in range(n + 1)]
    dp[0][0] = 0
    slider = deque([])

    def solve(i, j, slider: deque):
        s = j - R
        g = j - L
        if g < 0:
            dp[i][j] = dp[i - 1][j]
            return

        while slider and slider[0] <= s:    # ここが誤り
            slider.popleft()
        while slider and dp[i - 1][slider[-1]] < dp[i - 1][g]:
            slider.pop()
        slider.append(g)

        dp[i][j] = max(dp[i - 1][j], dp[i - 1][slider[0]] + dish)

    for i in range(1, n + 1):
        L, R, dish = randamDishes[i - 1]
        for j in range(w + 1):
            solve(i, j, slider)
        while slider:
            slider.pop()

    ans = dp[n][w]

    if ans == INF:
        return -1
    else:
        return ans


def simple():
    ans = 0
    for i in range(1, 2 ** n):
        low = 0
        high = 0
        v = 0
        for j in range(n):
            if (i >> j) & 1:
                L, R, dish = randamDishes[j - 1]
                low += L
                high += R
                v += dish
        if w >= low and w <= high:
            ans = max(ans, v)
    if ans == 0:
        ans = -1
    return ans


while 1:
    n = randint(1, 10)
    w = randint(1, 10)
    randamDishes = [[0] * 3 for _ in range(n)]
    for i in range(n):
        L = randint(1, w)
        R = randint(L, w)
        V = randint(1, 10)
        randamDishes[i] = (L, R, V)
    INF = -float("inf")

    ans1 = debug()
    ans2 = simple()
    if ans1 != ans2:
        print(f"{n=} {w=}")
        print(f"{randamDishes=}")
        print(f"{ans1=} {ans2=}")
        exit()
