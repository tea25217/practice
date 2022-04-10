import heapq


n, k, x = map(int, input().split())
a = list(map(int, input().split()))

cost = 0
remain = []
heapq.heapify(remain)

for i in a:
    use = min(i // x, k)
    cost_i = i - use * x
    cost += cost_i
    if cost_i != 0:
        heapq.heappush(remain, -cost_i)
    k -= use
while remain and k:
    c = -heapq.heappop(remain)
    cost -= c
    k -= 1

cost = max(cost, 0)
print(cost)
