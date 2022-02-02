from functools import reduce


_ = input()
a = map(int, input().split())


def gcd(a, b):
    n = max(a, b)
    d = min(a, b)
    if n % d == 0:
        return d
    return gcd(d, n % d)


ans = reduce(gcd, a)
print(ans)
