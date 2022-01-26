n, k = map(int, input().split())
acc = 0

for i in range(1, n + 1):
    for j in range(1, k + 1):
        acc += int(str(i) + '0' + str(j))

print(acc)
