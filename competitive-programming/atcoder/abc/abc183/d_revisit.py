# 解説を見ていもす法で実装

n, w = map(int, input().split())
TMAX = 2 * (10 ** 5) + 1

backets = [0] * (TMAX)

for i in range(n):
    s, t, p = map(int, input().split())
    backets[s] += p
    backets[t] -= p

cusum = 0

for j in range(TMAX):
    cusum += backets[j]
    if cusum > w:
        print('No')
        exit()

print('Yes')