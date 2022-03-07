n = int(input())
s = input()
a = "atcoder"
dp = [[0 for j in range(7)] for i in range(n + 1)]
M = 1000000007

for i in range(1, n + 1):
    for j in range(7):
        dp[i][j] = dp[i - 1][j]
        if j == 0:
            if s[i - 1] == a[j]:
                dp[i][j] += 1
        else:
            if s[i - 1] == a[j]:
                dp[i][j] += dp[i - 1][j - 1]
        dp[i][j] %= M

print(dp[n][6])
