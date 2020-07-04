import collections
import numpy as np

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def num_of_divisors(n):
    c = np.array(list(collections.Counter(prime_factorize(n)).values()))
    return np.prod(c + 1)

n = int(input())
ans = 0

for i in range(1, n+1):
    if i == 1:
        ans += 1
    else:
        ans += i * num_of_divisors(i)

print(ans)