n = int(input())
a = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

ans = set()

for j in range(2 ** n):
    acc = 0
    for k in range(n):
        if ((j >> k) & 1):
            acc += a[k]
    ans.add(acc)

for i in m:
    if i in ans:
        print("yes")
    else:
        print("no")
