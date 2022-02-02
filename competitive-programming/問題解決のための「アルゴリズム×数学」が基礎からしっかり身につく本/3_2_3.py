from functools import reduce


_ = input()
a = map(int, input().split())


def gcd(a, b):
    n = max(a, b)
    d = min(a, b)
    if n % d == 0:
        return d
    return gcd(d, n % d)


def lcm(a, b):
    return int((a * b) / gcd(a, b))


ans = reduce(lcm, a)
print(ans)
