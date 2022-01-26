import itertools

n, k = map(int, input().split())
table = [[int(j) for j in input().split()] for i in range(n)]
ans = 0

for i in itertools.permutations(range(2, n + 1)):
    route = list(i)
    route.insert(0, 1)
    route.append(1)
    dist = 0
    for j in range(len(route) - 1):
        dist += table[route[j] - 1][route[j+1] - 1]
    if dist == k:
        ans += 1

print(ans)