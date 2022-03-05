n = int(input())
dp = [[0 for j in range(10)] for i in range(n + 1)]
M = 998244353

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(1, 10):
        if j == 9:
            dp[i][j] = (dp[i- 1][j - 1] + dp[i- 1][j]) % M
        else:
            dp[i][j] = ((dp[i- 1][j - 1] + dp[i- 1][j]) % M + dp[i- 1][j + 1]) % M

ans = sum(dp[n]) % M
print(ans)
