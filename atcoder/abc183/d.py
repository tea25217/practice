# TLE answer

n, w = map(int, input().split())

backets = [0] * (2 * (10 ** 5))

for i in range(n):
    s, t, p = map(int, input().split())
    for j in range(s, t):
        backets[j-1] += p
        if backets[j-1] > w:
            print('No')
            exit()

print('Yes')