# 入力

# 入力が重い場合はsys.stdin.readline()を使う
# input()より速い
import sys

# foobar
s = input()
s = sys.stdin.readline()
# 1
n = int(input())
n = int(sys.stdin.readline())
# 1 2
a, b = map(int, input().split())
a, b = map(int, sys.stdin.readline().split())
# x1 x1
# x2 y2
# x3 y3
dots = [tuple(map(int, input().split())) for i in range(n)]
dots = [tuple(map(int, sys.stdin.readline().split())) for i in range(n)]
# a0 a1 a2 a3 a4
a = list(map(int, input().split()))
a = list(map(int, sys.stdin.readline().split()))
# a00 a01 a02 a03 a04
# a10 a11 a12 a13 a14
# a20 a21 a22 a23 a24
a = [list(map(int, input().split())) for i in range(n)]
a = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

# 出力
# 実行時間がギリギリな場合はsys.stdout.write()を使う
# print()より速い
sys.stdout.write(str(ans) + "\n")


# s[n] 初期値:0
backet = [0] * n
# s[n][m] 初期値:0
backet = [[0 for j in range(m)] for i in range(n)]


# 定数

# 素数
M = 998244353
M = 1000000007

# 逆元
Inv2 = 499122177    # mod 998244353における2の逆元
Inv2 = 500000004    # mod 1000000007における2の逆元


# 繰り返し二乗法
# (a ** b) mod divider
def modPow(a, b, divider):
    R = 30
    p = a
    ans = 1
    for i in range(R):
        if b & (1 << i):
            ans = (ans * p) % divider
        p = (p ** 2) % divider
    return ans


# 行列のt乗
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
t = 2
A_t = np.linalg.matrix_power(A, t)
print(A_t)


# 最大公約数・最小公倍数
# numpyを使う
import numpy as np

# 片方がリストの場合、数値の方とリストの要素ごとに計算
# リスト同士は要素ごとに計算
# 片方が0の場合はもう片方を返す
gcd1 = np.gcd(4, 6)     # 2
gcd2 = np.gcd(3, [3, 9, 15, 20])    # [3, 3, 3, 1]
gcd3 = np.gcd([0, 1, 2, 3], [2, 4, 6, 0])   # [2, 1, 2, 3]

# gcdと同様
lcm1 = np.lcm(4, 6)     # 12

# reduceメソッドを持ってる
lcmReduce = np.lcm.reduce([2, 3, 4])    # 12
gcdReduce = np.gcd.reduce([12, 6, 3], [6, 8, 0], [4, 3, 6])     # [2, 1, 3]


# NumPyでbit全探索する時のテンプレ

# (N以下の整数の中でV1..Vkいずれかの倍数であるものの個数を出力するプログラム)
# 以下をbit全探索
# V[j]の最小公倍数を出す。
# 立ってるbitの本数が奇数ならaccに足す。偶数なら引く。
import numpy as np

n, k = map(int, input().split())
v = np.array(list(map(int, input().split())))
acc = 0

for i in range(2 ** k):
    mask = np.array(list(map(lambda x: bool(int(x)), bin(i)[2:].zfill(k))))
    picked = v[mask]
    if len(picked) == 0:
        continue
    lcm_v = np.lcm.reduce(picked)
    num = n // lcm_v
    if len(picked) % 2 == 1:
        acc += num
    else:
        acc -= num

print(acc)


# 再帰回数の上限変更
from sys import setrecursionlimit
setrecursionlimit(1000000000)

# メモ化再帰
# @lru_cacheをつけるだけ
from functools import lru_cache

@lru_cache
def hoge(x):
    return hoge(x)


# 角度

# 偏角による角ABCの求め方
# 点A(x1, y1), 点B(x2, y2), 点C(x3, y3)があるとき
# 点Bを原点とみなした点A,Cの偏角をt1,t2とすると
ABC = min(abs(t1 - t2), 360 - abs(t1 - t2))
# 偏角tは
import math

t = math.atan2(y, x) * 180 / math.pi


# 部分集合の列挙
subsets = [[] for i in range(2 ** n)]
for i in range(1, 2 ** n):
    v = i
    while v:
        subsets[i].append(v)
        v = (v - 1) & i

# 部分集合の要素のインデックス列挙
# bit全探索で1の位置を前計算したくなった時用
subsetsIndexes = [[] for i in range(2 ** n)]
for i in range(1, 2 ** n):
    for j in range(n):
        if (i >> j) & 1:
            subsetsIndexes[i].append(j)


# 基数変換

# n進数 -> 10進数
n10 = int(n, 8)

# 10進数 -> n進数
import numpy as np

n9 = np.base_repr(n10, base=9)
