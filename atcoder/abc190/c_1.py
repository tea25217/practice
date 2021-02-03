# 提出コードと別ファイルでリファクタリング
# 復習のために解説URLを追記
# https://atcoder.jp/contests/abc190/editorial/626

n, m = map(int, input().split())
terms = [list(map(int, input().split())) for i in range(m)]
k = int(input())
dishes = [list(map(int, input().split())) for i in range(k)]

ans = 0

for i in range(2 ** k):
    isPut = [False] * n
    for j in range(k):
        if ((i >> j) & 1):
            isPut[dishes[j][0] - 1] = True
        else:
            isPut[dishes[j][1] - 1] = True

    acc = 0

    for j in range(m):
        isMatch = isPut[terms[j][0] - 1] and isPut[terms[j][1] - 1]
        if isMatch:
            acc += 1

    ans = max(ans, acc)

print(ans)
