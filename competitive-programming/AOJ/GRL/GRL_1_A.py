import heapq

v, e, r = map(int, input().split())
INF = 10 ** 9
dist = [INF] * v
adjacency_list = [[] for i in range(v)]

for i in range(e):
    s, t, d = map(int, input().split())
    adjacency_list[s].append((t, d))

dist[r] = 0
q = [(0, r)]
heapq.heapify(q)

while q:
    current_cost, current = heapq.heappop(q)

    if current_cost > dist[current]:
        continue

    for node, cost in adjacency_list[current]:
        if dist[node] > current_cost + cost:
            dist[node] = current_cost + cost
            heapq.heappush(q, (dist[node], node))

for i in range(v):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
