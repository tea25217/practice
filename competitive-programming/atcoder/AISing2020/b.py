n = int(input())
*a, = map(int, input().split())
ans = 0

for i in range(1, n + 1):
    if (i % 2) and (a[i-1] % 2):
        ans += 1

print(ans)