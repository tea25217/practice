import heapq

n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

q = []
heapq.heapify(q)

for i, e in enumerate(t):
    if i == n - 1:
        heapq.heappush(q, (e, 0))
    else:
        heapq.heappush(q, (e, i + 1))

remain = set(range(1, n + 1))
ans = [0] * n

while q:
    time, target = heapq.heappop(q)

    remain.discard(target)
    next = time + s[target - 1]

    if ans[target - 1] == 0:
        ans[target - 1] = time

    if len(remain) == 0:
        break

    if target == n:
        target = 0
    heapq.heappush(q, (next, target + 1))

for i in ans:
    print(i)
