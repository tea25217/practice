import heapq
import sys

n = int(sys.stdin.readline())

strings = set()
q = []
heapq.heapify(q)

for i in range(1, n + 1):
    s, t = input().split()
    t = int(t)
    if s in strings:
        continue
    strings.add(s)
    heapq.heappush(q, (-t + i * 10**-6, i))

print(q[0][1])
