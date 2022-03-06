# Mo's algorithm
n = int(input())
a = list(map(int, input().split()))
q = int(input())
blockSize = int(q ** 0.5 + 1)

# 1.各クエリのLを見てブロックに振り分ける
# 2.区間内はR昇順でソート
queryBlock = [[] for i in range(blockSize)]
for i in range(q):
    b = (*map(int, input().split()), i)
    # 0 <= L-1 <= n-1 のため、(b[0] - 1)部分をnで割ったら1未満、よって 0 <= 添字 < blocksize になる
    queryBlock[blockSize * (b[0] - 1) // n].append(b)
for i in range(blockSize):
    queryBlock[i].sort(key=lambda t: t[1])

backet = [0] * n
ans = [0] * q
l = 1
r = 1
backet[a[0] - 1] = 1
acc = 0


def increment(i):
    c = a[i - 1]
    backet[c - 1] += 1
    if backet[c - 1] % 2 == 0:
        return 1
    else:
        return 0


def decrement(i):
    c = a[i - 1]
    backet[c - 1] -= 1
    if backet[c - 1] % 2 == 1:
        return -1
    else:
        return 0


for queries in queryBlock:
    for newL, newR, queryNum in queries:
        if newR > r:
            for i in range(r + 1, newR + 1):
                acc += increment(i)
        if newR < r:
            for i in range(r, newR, -1):
                acc += decrement(i)
        r = newR

        if newL > l:
            for i in range(l, newL):
                acc += decrement(i)
        if newL < l:
            for i in range(l - 1, newL - 1, -1):
                acc += increment(i)
        l = newL
        ans[queryNum] = acc

for i in ans:
    print(i)
