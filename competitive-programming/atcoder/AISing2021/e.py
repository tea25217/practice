# 間に合わず

from collections import deque
from copy import deepcopy

n = int(input())
p = map(int, input().split())  # 添字アクセスするときは-2
adj = [[] for i in range(n + 1)]  # 添字アクセスそのまま
for i in range(2, n + 1):
    adj[i].append(p[i - 2])
    adj[p[i - 2]].append(i)

vertex = [[-1, []] for i in range(n + 1)]  # 添字アクセスそのまま、[距離, [経路]]

q = deque()
q.append([1, []])
vertex[1][0] = 0

while q:

    v, trace = q.popleft()
    trace.append(v)
    e = len(trace)
    for i in adj(v):
        if vertex[i][0] != -1:
            continue
        vertex[i][0] = e + 1
        vertex[i][1] = deepcopy(trace)
        q.append(i)

vertex = list(sorted(vertex))

Q = int(input())
    
for i in range(Q):
    u, d = map(int, input().split())