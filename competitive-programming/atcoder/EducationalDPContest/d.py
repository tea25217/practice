n, w_max = map(int, input().split())
w = []
v = []
for i in range(n):
    _w, _v = map(int, input().split())
    w.append(_w)
    v.append(_v)

dp = [[0] * (w_max + 1) for i in range(n + 1)]

for i in range(n):
    for j in range(w_max + 1):
        if j - w[i] >= 0:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - w[i]] + v[i])
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

ans = max(dp[n])

print(ans)
