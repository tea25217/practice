from collections import deque

n, m = map(int, input().split())
adj = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)


def dfs(start):
    d = deque([start])
    acc = 1
    seen = [False] * (n + 1)
    if len(adj[start]) == 0:
        return 1
    seen[start] = True

    while d:
        c = d.pop()
        for i in adj[c]:
            if seen[i]:
                continue
            seen[i] = True
            acc += 1
            d.append(i)

    return acc


ans = 0

for i in range(1, n + 1):
    ans += dfs(i)

print(ans)
