n = int(input())
grid = [[0 for j in range(1002)] for i in range(1002)]

for i in range(n):
    lx1, ly1, rx1, ry1 = map(int, input().split())
    grid[lx1][ly1] += 1
    grid[rx1][ry1] += 1
    grid[lx1][ry1] -= 1
    grid[rx1][ly1] -= 1

for i in range(1001):
    for j in range(1001):
        grid[i][j + 1] += grid[i][j]

for i in range(1001):
    for j in range(1001):
        grid[j + 1][i] += grid[j][i]

ans = [0] * (n + 1)

for i in range(1001):
    for j in range(1001):
        idx = grid[i][j]
        ans[idx] += 1

for i in range(1, n + 1):
    print(ans[i])
