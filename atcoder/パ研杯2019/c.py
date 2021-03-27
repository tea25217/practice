n, m = map(int, input(). split())
a = [list(map(int, input().split())) for i in range(n)]

ans = 0

for i in range(m - 1):
    for j in range(i + 1, m):
        if i == j:
            continue
        acc = 0

        for k in range(n):
            acc += max(a[k][i], a[k][j])

        ans = max(ans, acc)

print(ans)
