import sys

n, q = map(int, input().split())
NMAX = 200001
table = [0] * NMAX

for i in range(q):
    l, r = map(int, input().split())
    table[l - 1] += 1
    table[r] -= 1

cusum = 0

for i in range(n):
    cusum += table[i]
    if cusum % 2 == 0:
        sys.stdout.write('0')
    else:
        sys.stdout.write('1')

print()