import sys


n = int(sys.stdin.readline())
a = sorted(list(map(int, sys.stdin.readline().split())))
d = dict()
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

ans = 0

for i in range(n):
    for j in range(i, n):
        k = a[i] * a[j]
        if k > a[-1]:
            break
        t = 1 if i == j else 2
        if k in d:
            ans += d[k] * t

print(ans)
