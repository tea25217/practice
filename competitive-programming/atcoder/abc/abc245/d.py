from copy import deepcopy


n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
b = [0] * (m + 1)
mod = deepcopy(c)

for i in range(m, -1, -1):
    b[i] = mod[i + n] // a[-1]
    for j in range(n, -1, -1):
        mod[i + j] -= b[i] * a[j]

print(*b)
