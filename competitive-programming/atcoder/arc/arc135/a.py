# 解説AC
from functools import lru_cache


x = int(input())
M = 998244353


@lru_cache
def f(x):
    if x <= 4:
        return x
    x1 = x // 2
    x2 = (x + 1) // 2
    return f(x1) * f(x2) % M


print(f(x))
