n = input()
backet = [0] * 100000

for i in input().split():
    backet[int(i)] += 1

acc = 0

for i in range(1, (100000 // 2)):
    acc += backet[i] * backet[-i]

if backet[50000] <= 1:
    pass
else:
    acc += (backet[50000] * (backet[50000] - 1)) // 2

print(acc)
