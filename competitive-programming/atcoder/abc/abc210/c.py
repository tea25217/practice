n, k = map(int, input().split())
c = list(map(int, input().split()))
candy = {i: 0 for i in c}
dp = 0
ans = 0

for i in range(k):
    if candy[c[i]] == 0:
        dp += 1
    candy[c[i]] += 1

ans = dp

for i in range(k, n):
    candy[c[i - k]] -= 1
    if candy[c[i - k]] == 0:
        dp -= 1
    if candy[c[i]] == 0:
        dp += 1
    candy[c[i]] += 1
    ans = max(ans, dp)

print(ans)
