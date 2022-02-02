# 初期化条件が違った

import random


def compair():
    n = random.randint(1, 3)
    s = random.randint(1, 10)
    a = [random.randint(1, 10) for i in range(n)]

    def simple(n, s, a):
        for i in range(2**n):
            acc = 0
            for j in range(n):
                if (i >> j) & 1:
                    acc += a[j]
            if acc == s:
                return True

        return False

    def solver(n, s, a):
        dp = [[False for j in range(s + 1)] for i in range(n + 1)]

        dp[0][0] = True

        for i in range(1, n + 1):
            for j in range(1, s + 1):
                if j - a[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - a[i - 1]]

        return dp[n][s]

    if simple(n, s, a) != solver(n, s, a):
        print(f"n: {n}")
        print(f"s: {s}")
        print(f"a: {a}")
        exit()


if __name__ == '__main__':
    while 1:
        compair()
