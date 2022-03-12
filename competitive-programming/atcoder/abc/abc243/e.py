# コストがその辺以下の迂回路がある辺はいらない
n, m = map(int, input().split())
edge = [""] * m
for i in range(m):
    a, b, c = map(int, input().split())
    edge[i] = (a - 1, b - 1, c)
dist = [[float('inf') for j in range(n)] for i in range(n)]
for a, b, c in edge:
    dist[a][b] = c
    dist[b][a] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = 0
for a, b, c in edge:
    unused = False
    for i in range(n):
        if dist[a][i] + dist[i][b] <= c:
            unused = True
    if unused:
        ans += 1

print(ans)
