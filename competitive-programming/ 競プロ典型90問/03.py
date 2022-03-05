from collections import deque

n = int(input())
adj = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
seen = [False] * (n + 1)
q = deque([(1, 0)])
while q:
    c, dist = q.popleft()
    for i in adj[c]:
        if seen[i]:
            continue
        seen[i] = True
        q.append((i, dist + 1))

del q
del seen

seen = [False] * (n + 1)
q = deque([(c, 0)])

while q:
    c, dist = q.popleft()
    for i in adj[c]:
        if seen[i]:
            continue
        seen[i] = True
        q.append((i, dist + 1))

print(dist + 1)
