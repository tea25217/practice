from collections import deque


n, m = map(int, input().split())
color = [0] * n
adj = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b)
    adj[b - 1].append(a)


def dfs(i):
    color[i - 1] = 1
    q = deque([i])

    while q:
        v = q.popleft()
        c = color[v - 1]

        for j in adj[v - 1]:
            if not color[j - 1]:
                color[j - 1] = c * -1
                q.append(j)


for i in range(1, n + 1):
    if not color[i - 1]:
        dfs(i)


for i in range(1, n):
    for j in adj[i - 1]:
        if color[i - 1] == color[j - 1]:
            print("No")
            exit()

print("Yes")
