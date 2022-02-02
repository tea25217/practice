n = int(input())
dots = [[0 for j in range(2)] for i in range(n)]
for i in range(n):
    dots[i][0], dots[i][1] = map(int, input().split())

ans = 10 ** 12

for i in range(n - 1):
    for j in range(i + 1, n):
        dist = ((dots[i][0] - dots[j][0]) ** 2 + (dots[i][1] - dots[j][1]) ** 2) ** 0.5
        ans = min(ans, dist)

print(ans)
