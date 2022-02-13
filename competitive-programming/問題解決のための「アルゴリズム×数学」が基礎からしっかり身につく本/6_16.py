n, x = map(int, input().split())
ans = 0

for a in range(1, n - 1):
    for b in range(a + 1, n):
        c = x - a - b
        if c > b and c <= n:
            ans += 1

print(ans)
