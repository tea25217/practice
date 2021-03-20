n = int(input())
h = list(map(int, input().split()))
    
INF = 10 ** 9
dp = [INF] * n
dp[0] = 0
dp[1] = abs(h[0] - h[1])
    
for i in range(2, n):
    cost1 = abs(h[i-1] - h[i])
    cost2 = abs(h[i-2] - h[i])
    dp[i] = min(dp[i], dp[i-1] + cost1)
    dp[i] = min(dp[i], dp[i-2] + cost2)
    
print(dp[n-1])
