import heapq


n = int(input())
q = []
heapq.heapify(q)
for i in range(n):
    L, R = map(int, input().split())
    heapq.heappush(q, (R, L))

ans = 0
t = 0
while q:
    end, start = heapq.heappop(q)
    if start < t:
        continue
    ans += 1
    t = end

print(ans)
