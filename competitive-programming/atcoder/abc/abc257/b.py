n, k, q = map(int, input().split())
a = map(int, input().split())
L = map(int, input().split())

masu = [False] * (n + 1)

for i in a:
    masu[i] = True

for i in L:
    count = 0

    for j in range(1, n + 1):
        if masu[j]:
            count += 1
        if count == i:
            if j == n:
                break
            if masu[j + 1]:
                break
            masu[j + 1] = True
            masu[j] = False
            break

for i in range(n + 1):
    if masu[i]:
        print(i, end=" ")
