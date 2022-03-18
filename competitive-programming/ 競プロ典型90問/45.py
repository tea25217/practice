# まだワーストケースが通らない
n, k = map(int, input().split())
dots = [""] * n
for i in range(n):
    x, y = map(int, input().split())
    dots[i] = (x, y)

# 二点間距離
d2 = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        d2[i][j] = abs(dots[i][0] - dots[j][0]) ** 2 + abs(dots[i][1] - dots[j][1]) ** 2

# 部分集合の二点間距離最大値
dist = [0] * 2 ** n
for i in range(1, 2 ** n):
    dj = 0
    for j in range(n):
        if (i >> j) & 1:
            for m in range(n):
                if (i >> m) & 1:
                    dj = max(dj, d2[j][m])
    dist[i] = dj

# 部分集合の列挙
subsets = [[] for i in range(2 ** n)]
for i in range(1, 2 ** n):
    v = i
    while v:
        subsets[i].append(v)
        v = (v - 1) & i

# bitDP
INF = float('inf')
dp = [[INF] * (k + 1) for i in range(2 ** n)]
dp[0][0] = 0
for j in range(1, k + 1):
    for i in range(1, 2 ** n):
        minDist = INF
        for b in subsets[i]:
            d = max(dp[i - b][j - 1], dist[b])
            minDist = min(minDist, d)
        dp[i][j] = minDist

print(dp[2 ** n - 1][k])
