n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

acc = 0

for x in range(1, 1001):
    for i in range(n):
        if (a[i] > x) or (b[i] < x):
            break
    else:
        acc += 1

print(acc)
