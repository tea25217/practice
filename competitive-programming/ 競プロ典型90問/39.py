# 各辺を通る回数は両側の頂点数の積
# 枝にぶら下がる頂点数をaとすると、その枝を通る回数はa * a(n - a)
# これを戻りがけで数えればいい
from sys import setrecursionlimit
setrecursionlimit(100000)


n = int(input())
adj = [[] for _ in range(n + 1)]
for i in range(1, n):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
seen = [False] * (n + 1)


def dfs(i):
    if len(adj[i]) == 1 and seen[adj[i][0]]:
        return (1, 0)

    nodes = 1
    ans = 0

    for j in adj[i]:
        if seen[j]:
            continue
        seen[j] = True
        k, a = dfs(j)
        nodes += k
        ans += a
        ans += k * (n - k)

    return (nodes, ans)


_, ans = dfs(1)
print(ans)
