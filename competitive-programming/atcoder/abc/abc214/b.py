s, t = map(int, input().split())

acc = 0

for i in range(s + 1):
    for j in range(s + 1):
        for k in range(s + 1):
            if (i + j + k > s) or (i * j * k > t):
                continue
            acc += 1

print(acc)
