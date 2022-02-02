n, s = map(int, input().split())
a = list(map(int, input().split()))


def solver(n, s, a):
    dp = [[False for j in range(s + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, s + 1):
            if j - a[i - 1] < 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - a[i - 1]]

    return dp[n][s]


acc = solver(n, s, a)

if acc:
    print("Yes")
else:
    print("No")
