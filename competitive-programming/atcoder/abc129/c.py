n, m = map(int, input().split())
broken = [False] * (n + 2)
for i in range(m):
    a = int(input())
    broken[a] = True

dp = [0] * (n + 2)
dp[0] = 1
if not broken[1]:
    dp[1] = 1

for i in range(2, n + 1):
    if broken[i - 1] and broken[i - 2]:
        print(0)
        exit()
    if broken[i]:
        continue
    dp[i] = dp[i - 1] + dp[i - 2]
     
ans = dp[n] % 1000000007

print(ans)
