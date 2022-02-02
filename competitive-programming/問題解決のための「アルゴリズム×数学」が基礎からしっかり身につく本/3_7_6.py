n = int(input())
a = list(map(int, input().split()))

dp = [[0 for j in range(2)] for i in range(n + 1)]

dp[0][0] = dp[0][1] = 0

for i in range(1, n + 1):
    for j in range(2):
        if j == 0:
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
        else:
            dp[i][1] = a[i - 1] + dp[i - 1][0]

ans = max(dp[n])

print(ans)
