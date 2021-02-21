import sys
from heapq import heappush, heappop

INF = sys.maxsize

n, m, x, y = map(int, input().split())

# 都市aの隣接リスト
# adjacent[a]==(都市b, (所要時間t, 出発時刻==kの倍数))
adjacent = [[] for _ in range(n)]
for i in range(m):
    a, b, t, k = map(int, input().split())
    adjacent[a - 1].append((b, (t, k)))
    adjacent[b - 1].append((a, (t, k)))


def arrival(now, t, k):
    return (((now + k - 1) // k) * k) + t


def dijkstra():
    arrivalTime = [INF] * n
    isVisited = [False] * n
    arrivalTime[x - 1] = 0
    q = [(0, x)]

    while q:
        current = heappop(q)[1]

        if current == y:
            return arrivalTime[y - 1]
        if isVisited[current - 1]:
            continue

        isVisited[current - 1] = True
        now = arrivalTime[current - 1]

        for to, time in adjacent[current - 1]:
            calcedArrival = arrival(now, time[0], time[1])
            if calcedArrival < arrivalTime[to - 1]:
                arrivalTime[to - 1] = calcedArrival
                heappush(q, (arrivalTime[to - 1], to))

    if arrivalTime[y - 1] != INF:
        return arrivalTime[y - 1]
    else:
        return -1


ans = dijkstra()
print(ans)
