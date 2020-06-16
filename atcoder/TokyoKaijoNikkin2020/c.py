# TLE
import copy

n, k = map(int, input().split())
*lumen, = list(map(int, input().split()))
lamps = [set() for i in range(n)]

for h in range(k):
    num_of_lamps = [0] * n

    for i in range(1, n+1):
        x_min = i - lumen[i-1]
        x_max = i + lumen[i-1]
        if x_min < 1:
            x_min = 1
        if x_max > n:
            x_max = n
        for j in range(x_min, x_max+1):
            num_of_lamps[j-1] += 1

    lumen = copy.copy(num_of_lamps)

lumen = ' '.join(list(map(str,lumen)))
print(lumen)