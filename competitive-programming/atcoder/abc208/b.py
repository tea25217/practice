p = int(input())

coins = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
acc = 0

for c in coins[::-1]:
    for j in range(100):
        if p >= c:
            p -= c
            acc += 1
        else:
            break
    if p == 0:
        break

print(acc)
