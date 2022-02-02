n, q = map(int, input().split())
a = list(map(int, input().split()))
l = [0] * q
r = [0] * q
for i in range(q):
    l[i], r[i] = map(int, input().split())

b = [0] * (n + 1)

for i, e in enumerate(a):
    b[i + 1] = b[i] + e

for i in range(q):
    ans = b[r[i]] - b[l[i] - 1]
    print(ans)
