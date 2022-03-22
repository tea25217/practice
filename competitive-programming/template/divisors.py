# 約数列挙
from copy import deepcopy
from math import floor
from typing import List


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
