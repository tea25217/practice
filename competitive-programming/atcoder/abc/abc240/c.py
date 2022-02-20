n, x = map(int, input().split())
dp = [[False for j in range(10001)] for i in range(n + 1)]
dp[0][0] = True

for i in range(1, n + 1):
    a, b = map(int, input().split())
    for j in range(x + 1):
        if j - a < 0:
            dp[i][j] = dp[i - 1][j - b]
        elif j - b < 0:
            dp[i][j] = dp[i - 1][j - a]
        else:
            dp[i][j] = dp[i - 1][j - b] or dp[i - 1][j - a]

if dp[n][x]:
    print("Yes")
else:
    print("No")
