n, r = map(int, input().split())


def combination(n, r):
    fact = lambda n: 1 if n <= 1 else n * fact(n - 1)

    return int(fact(n) / (fact(r) * fact(n - r)))


ans = combination(n, r)

print(ans)
