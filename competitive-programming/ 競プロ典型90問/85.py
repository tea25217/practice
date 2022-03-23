from copy import deepcopy
from math import floor
from typing import List


k = int(input())


def getDivisors(k: int) -> List[int]:
    """generete divisor list

    Args:
        k (int): natural number

    Returns:
        List[int]: divisors of k
    """
    d = []
    for i in range(1, floor(k ** 0.5) + 1):
        if (k % i):
            continue
        d.append(i)
        if i != (k // i):
            d.append(k // i)
    return deepcopy(d)


d = sorted(getDivisors(k))
ans = 0
for i in range(len(d)):
    for j in range(i, len(d)):
        if k // d[i] < d[j]:
            continue
        if k % (d[i] * d[j]):
            continue
        if d[j] <= k // (d[i] * d[j]):
            ans += 1
print(ans)
