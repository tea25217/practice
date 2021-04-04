# 色々見ながら練習
# 問題 https://atcoder.jp/contests/abc190/tasks/abc190_f
# 解説 https://atcoder.jp/contests/abc190/editorial/631
# Binary indexed tree
# https://www.slideshare.net/hcpc_hokudai/binary-indexed-tree

N = int(input())
A = list(map(int, input().split()))

# 0始まりだと扱い辛いため1始まりに補正
A = [i + 1 for i in A]


# Least Significant Bit
# 2進表記した際に1が立っている最も右側のビットのみ残し、他のビットは0になった値を返す
# ex. 6(0b0110) → 2(0b0010)
def LSB(i):
    return i & (-i)


# a1 + a2 + ... + aiの計算
# BITの添字からLSBを減算しながら対象となった箇所を足していく
def sum_BIT(BIT, i):
    acc = 0
    while i:
        acc += BIT[i]
        i -= LSB(i)
    return acc


# aiにxを足す
# BITの添字にLSBを加算しながら対象となった箇所へ足していく
def add_BIT(BIT, i, x):
    while i <= N:
        BIT[i] += x
        i += LSB(i)


def count_inversion_number(arr):
    BIT = [0] * (N + 1)
    acc = 0

    for j in range(0, N):
        acc += j - sum_BIT(BIT, arr[j])
        add_BIT(BIT, arr[j], 1)

    return acc


def diff_for_inversion_numbers_by_k(i):
    return N - 1 - 2 * i


def solver():
    ans = count_inversion_number(A)
    for i in A:
        print(ans)
        ans += diff_for_inversion_numbers_by_k(i - 1)


solver()
