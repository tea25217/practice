from math import floor


n = int(input())

for i in range(floor(n ** 0.5), 0, - 1):
    if n % i == 0:
        ans = ((n // i) + i) * 2
        print(ans)
        exit()
