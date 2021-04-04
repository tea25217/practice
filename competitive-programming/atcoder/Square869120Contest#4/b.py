# 実装方針は合ってそうだけどWAが1個取れない

from copy import deepcopy

n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 10 ** 10

for i in range(2 ** n):
    tall = a[0]
    acc = 0
    b = deepcopy(a)
    for j in range(1, n):
        if not ((i >> j) & 1):
            tall = max(tall, a[j])
        else:
            if a[j] > tall:
                tall = a[j]
            else:
                cost = tall - a[j] + 1
                acc += cost
                tall += 1
                b[j] = tall
    view = 1
    tall = a[0]
    for j in range(1, n):
        if b[j] > tall:
            view += 1
            tall = b[j]
    if view >= k:
        ans = min(ans, acc)

print(ans)
