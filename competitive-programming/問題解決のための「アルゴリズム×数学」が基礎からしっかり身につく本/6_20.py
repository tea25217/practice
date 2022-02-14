n = int(input())
cusum1 = [0] * (n + 1)
cusum2 = [0] * (n + 1)

for i in range(1, n + 1):
    c, p = map(int, input().split())
    if c == 1:
        cusum1[i] = cusum1[i - 1] + p
        cusum2[i] = cusum2[i - 1]
    else:
        cusum2[i] = cusum2[i - 1] + p
        cusum1[i] = cusum1[i - 1]

for _ in range(int(input())):
    L, R = map(int, input().split())
    a1 = cusum1[R] - cusum1[L - 1]
    a2 = cusum2[R] - cusum2[L - 1]
    print(a1, a2)
