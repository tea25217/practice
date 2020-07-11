import math

n = int(input())

for i in range(1, n + 1):
    cnt = 0
    t = math.floor(i - (i ** 0.5)) + 1
    for j in range(1, t):
        for k in range(1, t):
            for l in range(1, t):
                if ((j ** 2) + (k ** 2) + (l ** 2) + (j * k) + (k * l) + (l * j)) == i:
                    cnt += 1
                elif ((j ** 2) + (k ** 2) + (l ** 2) + (j * k) + (k * l) + (l * j)) > i:
                    break
                else:
                    pass
    print(cnt)