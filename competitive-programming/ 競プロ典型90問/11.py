n = int(input())
tasks = [""] * n
for i in range(n):
    d, c, s = map(int, input().split())
    tasks[i] = (d, c, s)
tasks.sort()
# もらうDP dp[何件目まで判断したか][何日仕事したか]
dp = [[0 for j in range(5001)] for i in range(n + 1)]

for i in range(1, n + 1):
    d, c, s = tasks[i - 1]

    for j in range(5001):
        # もらえない場合
        # 所要日数未満しか仕事してない or 締切を過ぎている
        # => その仕事はしていないはず
        if (j < c) or (d < j):
            dp[i][j] = dp[i - 1][j]
        # もらえる場合
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - c] + s)

ans = max(dp[n])
print(ans)
