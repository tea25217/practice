n = int(input())
*t, = map(int, input().split())

sum_T = sum(t)
dp = [[False for j in range(sum_T + 1)] for i in range(n + 1)]
dp[0][0] = True

for i in range(1, n + 1):
    for j in range(sum_T + 1):
        if j - t[i - 1] < 0:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j] or dp[i - 1][j - t[i - 1]]

set_Ta = set()
for j in range(sum_T + 1):
    if dp[n][j]:
        set_Ta.add(j)

ans = sum_T
for ta in set_Ta:
    tt = max(ta, sum_T - ta)
    ans = min(ans, tt)

print(ans)
