n = int(input())
f = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(i, n + 1, i):
        f[j] += 1

ans = 0

for i in range(1, n + 1):
    ans += i * f[i]

print(ans)
