from itertools import permutations
from math import factorial

n = int(input())
x = []
y = []
for i in range(n):
    ix, iy = map(int, input().split())
    x.append(ix)
    y.append(iy)

patterns = permutations(range(n), n)
ans = 0

for i in patterns:
    for j in range(1, len(i)):
        a, b = i[j - 1], i[j]
        d = ((x[a] - x[b]) ** 2 + (y[a] - y[b]) ** 2) ** 0.5
        ans += d

p = factorial(n)
ans /= p

print(ans)
