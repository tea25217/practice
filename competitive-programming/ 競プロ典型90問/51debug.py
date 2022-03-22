# 31行目ソートできてなかった
# (mapオブジェクト作っとるだけやった…)
from random import randint
from typing import List
from bisect import bisect_right
from copy import deepcopy


def solve():
    h = n // 2
    a1 = a[:h]
    a2 = a[h:]

    # 全探索してバケツを返す
    def pick(item: List[int]) -> List[List[int]]:
        bucket = [[] for i in range(n + 1)]
        L = len(item)
        for i in range(2 ** L):
            m = 0
            v = 0
            for j in range(L):
                if (i >> j) & 1:
                    m += 1
                    v += item[j]
            if v <= p and m <= k:
                bucket[m].append(v)
        return deepcopy(bucket)

    b1 = pick(a1)
    b2 = pick(a2)
    map(lambda a: a.sort(), b2)

    acc = 0
    for k1 in range(n + 1):
        for value1 in b1[k1]:
            num2 = bisect_right(b2[k - k1], p - value1)
            acc += num2

    return acc


def simple():
    acc = 0
    for i in range(2 ** n):
        m = 0
        v = 0
        for j in range(n):
            if (i >> j) & 1:
                m += 1
                v += a[j]
        if v <= p and m == k:
            acc += 1
    return acc


while 1:
    n = randint(1, 10)
    k = randint(1, n)
    p = randint(1, 10)
    a = [randint(1, 10) for _ in range(n)]

    ans1 = solve()
    ans2 = simple()
    if ans1 != ans2:
        print(f"{n=} {k=} {p=}")
        print(f"{a=}")
        print(f"{ans1=} {ans2=}")
        exit()
