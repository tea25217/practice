n = int(input())
*b, = map(int, input().split())

ans = b[0]

for i in range(1, n - 1):
    ans += min(b[i - 1], b[i])

ans += b[n - 2]

print(ans)
