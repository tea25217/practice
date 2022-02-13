a, b = map(int, input().split())


def gcd(a, b):
    n = max(a, b)
    d = min(a, b)
    if n % d == 0:
        return d
    return gcd(d, n % d)


def lcm(a, b):
    return int((a // gcd(a, b)) * b)


ans = lcm(a, b)
if ans > 10 ** 18:
    print("Large")
else:
    print(ans)
