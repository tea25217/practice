r, c = map(int, input().split())
senbei = [list(map(int, input().split())) for _ in range(r)]
ans = 0

for i in range(2 ** r):
    mask = []
    for j in range(r):
        mask.append(((i >> j) & 1))
    acc = 0
    for j in range(c):
        acc_col = 0
        for k in range(r):
            acc_col += senbei[k][j] ^ mask[k]
        if acc_col < (r / 2):
            acc_col = r - acc_col
        acc += acc_col
    ans = max(ans, acc)

print(ans)
