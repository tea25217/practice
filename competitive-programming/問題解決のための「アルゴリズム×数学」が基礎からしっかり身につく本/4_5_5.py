n, m = map(int, input().split())
v = [0] * n
for i in range(m):
    a, b = map(int, input().split())
    if a > b:
        v[a - 1] += 1
    if b > a:
        v[b - 1] += 1

ans = sum([1 if i == 1 else 0 for i in v])
print(ans)
