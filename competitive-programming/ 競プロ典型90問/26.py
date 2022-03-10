from collections import deque


n = int(input())
adj = [[] for i in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

odd = []
even = []

seen = [False] * (n + 1)
q = deque([(1, 0)])
seen[1] = True

while q:
    c, d = q.popleft()
    if d % 2 == 1:
        odd.append(c)
    else:
        even.append(c)

    for i in adj[c]:
        if seen[i]:
            continue
        seen[i] = True
        q.append((i, d + 1))


def ans(s):
    n = len(s)
    for i in range(n):
        print(s[i], end="")
        if i < n - 1:
            print(" ", end="")


if len(odd) > len(even):
    ans(odd[:n // 2])
else:
    ans(even[:n // 2])
