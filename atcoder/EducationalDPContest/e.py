n, w_max = map(int, input().split())
w = []
v = []
for i in range(n):
    _w, _v = map(int, input().split())
    w.append(_w)
    v.append(_v)

v_max = n * 10 ** 3 + 1
INF = 10 ** 9 + 1

dp = [[INF] * (v_max) for i in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(v_max):
        if j - v[i] >= 0:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - v[i]] + w[i])
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])



for i in range(v_max - 1, -1, -1):
    if dp[n][i] <= w_max:
        print(i)
        exit()
