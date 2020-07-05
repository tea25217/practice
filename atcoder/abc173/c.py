import copy

h, w, k = map(int, input().split())
table = [0]*h
for i in range(h):
    table[i] = [0 if j == "." else 1 for j in input()]
ans = 0

for i in range(2 ** (h + w)):
    t = copy.deepcopy(table)
    for j in range(h + w):
        if ((i >> j) & 1):
            if j < h:
                for l in range(w):
                    t[j][l] = 0
            else:
                for l in range(h):
                    t[l][j-h] = 0
    black = sum(map(sum, t))
    if black == k:
        ans += 1

print(ans)