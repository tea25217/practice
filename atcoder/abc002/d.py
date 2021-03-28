from itertools import combinations

n, m = map(int, input().split())
kone = set()
for i in range(m):
    x, y = map(int, input().split())
    kone.add((x, y))

ans = 1

for i in range(2 ** n):
    hito = []
    for j in range(n):
        if ((i >> j) & 1):
            hito.append(j + 1)
    if len(hito) <= 1:
        continue
    pairs = combinations(hito, 2)
    for x, y in pairs:
        if not ((x, y) in kone) or ((y, x) in kone):
            break
    else:
        ans = max(ans, len(hito))

print(ans)
