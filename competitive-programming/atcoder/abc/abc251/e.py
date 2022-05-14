import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
INF = float("INF")
ans = [0] * 8

# A(N)を払わないケース
dp1 = [[0] * 2 for i in range(n + 1)]
dp1[1][0] = INF
dp1[1][1] = a[1 - 1]

for i in range(2, n + 1):
    dp1[i][0] = dp1[i - 1][1]
    dp1[i][1] = min(dp1[i - 1][0], dp1[i - 1][1]) + a[i - 1]


# A(N)を払うケース
dp2 = [[0] * 2 for i in range(n + 1)]
dp2[0][0] = INF
dp2[0][1] = a[n - 1]

for i in range(1, n + 1):
    dp2[i][0] = dp2[i - 1][1]
    dp2[i][1] = min(dp2[i - 1][0], dp2[i - 1][1]) + a[i - 1]

# 逆順
a = a[::-1]
ans[0] = dp1[n][0]
ans[1] = dp2[n][1]
del dp1
del dp2

# A(N)を払わないケース
dp1 = [[0] * 2 for i in range(n + 1)]
dp1[1][0] = INF
dp1[1][1] = a[1 - 1]

for i in range(2, n + 1):
    dp1[i][0] = dp1[i - 1][1]
    dp1[i][1] = min(dp1[i - 1][0], dp1[i - 1][1]) + a[i - 1]


# A(N)を払うケース
dp2 = [[0] * 2 for i in range(n + 1)]
dp2[0][0] = INF
dp2[0][1] = a[n - 1]

for i in range(1, n + 1):
    dp2[i][0] = dp2[i - 1][1]
    dp2[i][1] = min(dp2[i - 1][0], dp2[i - 1][1]) + a[i - 1]

ans[2] = dp1[n][0]
ans[3] = dp2[n][1]


# 配列ずらし
del dp1
del dp2
a = a[1:] + a[:1]

# A(N)を払わないケース
dp1 = [[0] * 2 for i in range(n + 1)]
dp1[1][0] = INF
dp1[1][1] = a[1 - 1]

for i in range(2, n + 1):
    dp1[i][0] = dp1[i - 1][1]
    dp1[i][1] = min(dp1[i - 1][0], dp1[i - 1][1]) + a[i - 1]


# A(N)を払うケース
dp2 = [[0] * 2 for i in range(n + 1)]
dp2[0][0] = INF
dp2[0][1] = a[n - 1]

for i in range(1, n + 1):
    dp2[i][0] = dp2[i - 1][1]
    dp2[i][1] = min(dp2[i - 1][0], dp2[i - 1][1]) + a[i - 1]

# 逆順
a = a[::-1]
ans[4] = dp1[n][0]
ans[5] = dp2[n][1]
del dp1
del dp2

# A(N)を払わないケース
dp1 = [[0] * 2 for i in range(n + 1)]
dp1[1][0] = INF
dp1[1][1] = a[1 - 1]

for i in range(2, n + 1):
    dp1[i][0] = dp1[i - 1][1]
    dp1[i][1] = min(dp1[i - 1][0], dp1[i - 1][1]) + a[i - 1]


# A(N)を払うケース
dp2 = [[0] * 2 for i in range(n + 1)]
dp2[0][0] = INF
dp2[0][1] = a[n - 1]

for i in range(1, n + 1):
    dp2[i][0] = dp2[i - 1][1]
    dp2[i][1] = min(dp2[i - 1][0], dp2[i - 1][1]) + a[i - 1]

ans[6] = dp1[n][0]
ans[7] = dp2[n][1]

print(min(ans))
