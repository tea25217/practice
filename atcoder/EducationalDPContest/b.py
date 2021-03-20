INF = 10 ** 5

n, k = map(int, input().split())
h = list(map(int, input().split())) + [INF] * (k)

dp = [INF] * (n + k)
dp[0] = 0

for i in range(n):
    for j in range(1, k + 1):
        cost = abs(h[i] - h[i + j])
        if (dp[i] + cost) >= dp[i + j]:
            continue
        dp[i + j] = dp[i] + cost

print(dp[n - 1])
