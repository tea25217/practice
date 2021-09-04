n = int(input())
p = [0] + list(map(int, input().split()))

q = [0] * (n + 1)

for i, num in enumerate(p):
    q[p[i]] = i

for i in range(1, n + 1):
    print(q[i], end='')
    if i != n:
        print(' ', end='')
    else:
        print('')
