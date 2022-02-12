# 重み付き無向グラフのダイクストラ法
import heapq

n, m = map(int, input().split())
adj = [[] for i in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((c, b))
    adj[b].append((c, a))

INF = 10 * 10**10
dist = [INF] * (n + 1)
dist[1] = 0
done = [False] * (n + 1)

q = [(0, 1)]
heapq.heapify(q)

while q:
    cost, node = heapq.heappop(q)
    if done[node]:
        continue
    done[node] = True

    for c, nextNode in adj[node]:
        nextCost = cost + c
        if dist[nextNode] > nextCost:
            dist[nextNode] = nextCost
            heapq.heappush(q, (nextCost, nextNode))

ans = dist[n]
if dist[n] == INF:
    ans = -1

print(ans)
