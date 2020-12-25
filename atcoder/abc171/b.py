n, k = map(int, input().split())
*p, = sorted(map(int, input().split()))

ans = sum(p[:k])

print(ans)