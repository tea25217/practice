n = int(input())
*a, = sorted(map(int, input().split()))
a_max = a[n-1]
dp = [True] * a_max
ans = 0
recent = 0

if n == 1:
    print(1)
    exit()

for i in a:
    if recent == i:
        ans -= 1
        recent = 0
    if dp[i-1] == False:
        continue
    else:
        for j in range(i, a_max+1, i):
            dp[j-1] = False
        ans += 1
        recent = i

print(ans)