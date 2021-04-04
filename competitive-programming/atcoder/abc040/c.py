n = int(input())
a = list(map(int, input().split())) + [0, 0]

INF = n * 10 ** 4 + 1
dp = [INF] * (n + 2)
dp[0] = 0

for i in range(n):
    cost1 = abs(a[i] - a[i + 1])
    cost2 = abs(a[i] - a[i + 2])
    dp[i + 1] = min(dp[i + 1], dp[i] + cost1)
    dp[i + 2] = min(dp[i + 2], dp[i] + cost2)

print(dp[n - 1])
