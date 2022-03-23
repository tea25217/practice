n, m, k, s, t, x = map(int, input().split())
M = 998244353
adj = [[] for i in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

dp = [[[0] * 2 for j in range(n + 1)] for i in range(k + 1)]
dp[0][s][0] = 1

for i in range(1, k + 1):
    for j in range(1, n + 1):
        if j != x:
            for m in (0, 1):
                for node in adj[j]:
                    dp[i][j][m] = (dp[i][j][m] + dp[i - 1][node][m]) % M
        else:
            for m in (0, 1):
                for node in adj[j]:
                    dp[i][j][int(not m)] = (dp[i][j][int(not m)] + dp[i - 1][node][m]) % M

print(dp[k][t][0])
