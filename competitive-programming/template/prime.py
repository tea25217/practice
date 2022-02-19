from math import floor
from typing import Iterable
import numpy as np


def isPrime(n: int) -> bool:
    """試し割り法

    Args:
        n (int): 対象の整数

    Returns:
        _bool: 素数かどうか
    """
    if n <= 1:
        return False
    for i in range(2, floor(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generateBoolPrimeList(n: int) -> Iterable[bool]:
    """ Generate boolean list of prime number by Sieve of Eratosthenes

    Args:
        n (int): max number (n >= 3)

    Returns:
        ndarray[bool]: prime number or not
    """
    n += 1
    prime = np.zeros(n, dtype="bool")
    prime[2] = True
    prime[3::2] = True

    for i in range(3, floor(n ** 0.5) + 1, 2):
        if prime[i]:
            prime[i ** 2::2 * i] = False

    return prime


def generatePrimeList(n: int) -> Iterable[int]:
    """ Generate prime number list

    Args:
        n (int): max number (n >= 3)

    Returns:
        ndarray[int]: prime number list
    """
    return np.where(generateBoolPrimeList(n))[0]
