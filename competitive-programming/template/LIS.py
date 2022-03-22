from bisect import bisect_left
from copy import deepcopy
from typing import List


def getLIS(a: List[int]) -> int:
    """calculate length of Longest Increase Subsequence

    Args:
        a (List[int]): integer sequence

    Returns:
        int: length of LIS
    """
    n = len(a)
    if not n:
        return []

    LIS = [a[0]]
    for i in range(1, n):
        if a[i] > LIS[-1]:
            LIS.append(a[i])
        else:
            idx = bisect_left(LIS, a[i])
            LIS[idx] = a[i]

    return len(LIS)


def getLISList(a: List[int]) -> List[int]:
    """calculate length of Longest Increase Subsequence

    Args:
        a (List[int]): integer sequence

    Returns:
        List[int]: LIS length of [0,i]
    """
    n = len(a)
    if not n:
        return []

    LIS = [a[0]]
    ans = [0] * n
    for i in range(n):
        if a[i] > LIS[-1]:
            LIS.append(a[i])
        else:
            idx = bisect_left(LIS, a[i])
            LIS[idx] = a[i]
        ans[i] = len(LIS)

    return deepcopy(ans)
