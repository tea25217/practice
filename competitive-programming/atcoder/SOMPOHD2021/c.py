n, k = map(int, input().split())


def g1(n):
    return int("".join(sorted(str(n), reverse=True)))


def g2(n):
    return int("".join(sorted(str(n))))


def f(n):
    return g1(n) - g2(n)


ans = n

for i in range(k):
    ans = f(ans)

print(ans)
