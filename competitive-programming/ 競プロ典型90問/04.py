h, w = map(int, input().split())
masu = [list(map(int, input().split())) for i in range(h)]
rowSum = [0] * h
colSum = [0] * w

for i in range(h):
    for j in range(w):
        rowSum[i] += masu[i][j]
        colSum[j] += masu[i][j]

for i in range(h):
    for j in range(w):
        ans = rowSum[i] + colSum[j] - masu[i][j]
        print(ans, end="")
        if j != w - 1:
            print(" ", end="")
    print()
