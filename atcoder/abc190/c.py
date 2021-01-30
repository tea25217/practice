# 復習のために解説URLを追記
# https://atcoder.jp/contests/abc190/editorial/626

n, m = map(int, input().split())
terms = [[0 for j in range(2)] for i in range(m)]
for i in range(m):
    a, b = map(int, input().split())
    terms[i][0] = a
    terms[i][1] = b
k = int(input())
dishes = [[0 for j in range(2)] for i in range(k)]
for i in range(k):
    c, d = map(int, input().split())
    dishes[i][0] = c
    dishes[i][1] = d

ans = 0

for i in range(2 ** k):
    isPut = [False] * n
    for j in range(k):
        if ((i >> j) & 1):
            isPut[dishes[j][0] -1] = True
        else:
            isPut[dishes[j][1] -1] = True

    acc = 0

    for j in range(m):
        if isPut[terms[j][0] -1] and isPut[terms[j][1] -1]:
            acc += 1

    ans = max(ans, acc)

print(ans)
