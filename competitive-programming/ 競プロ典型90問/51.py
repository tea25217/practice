# 半分全列挙
# a1,a2を全探索し結果を個数のバケツに入れる
# バケツ2の中身をソート
# バケツ1の各要素に対し、バケツ2[不足個数]の中身を二分探索して合計P円以下の通り数を取得
from typing import List
from bisect import bisect_right
from copy import deepcopy


n, k, p = map(int, input().split())
a = list(map(int, input().split()))
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
[x.sort() for x in b2]

acc = 0
for k1 in range(n + 1):
    for value1 in b1[k1]:
        num2 = bisect_right(b2[k - k1], p - value1)
        acc += num2

print(acc)
