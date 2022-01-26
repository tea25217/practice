from itertools import permutations

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

patterns = list(sorted(list(permutations(range(1, n + 1), n))))

for i in range(len(patterns)):
    if patterns[i] == p:
        np = i + 1
    if patterns[i] == q:
        nq = i + 1

ans = abs(np - nq)

print(ans)
