# input

# foobar
s = input()
# 1
n = int(input())
# 1 2
a, b = map(int, input().split())
# a0 a1 a2 a3 a4
a = list(map(int, input().split()))
# a00 a01 a02 a03 a04
# a10 a11 a12 a13 a14
# a20 a21 a22 a23 a24
a = [list(map(int, input().split())) for i in range(n)]

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


# mod M におけるnの逆元

# mod Mの世界では÷nを×toInverseElement(n)に置き換える
# 前提1：Mとaが互いに素であること（逆元が存在する条件）
# 前提2：Mが素数であること（フェルマーの小定理を用いた方法のため）
# 素数以外で使う場合は拡張ユークリッドの互除法で実装し直す
def toInverseElement(M, n):

    # 繰り返し二乗法で (a ** b) mod dividerを求める関数
    def modPow(a, b, divider):
        R = 30
        p = a
        ans = 1
        for i in range(R):
            if b & (1 << i):
                ans = (ans * p) % divider
            p = (p ** 2) % divider
        return ans

    return modPow(n, M - 2, M)


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
setrecursionlimit(2000)

# メモ化再帰
# @lru_cacheをつけるだけ
from functools import lru_cache


@lru_cache
def hoge(x):
    return hoge(x)


# 行列のt乗
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
t = 2
A_t = np.linalg.matrix_power(A, t)
print(A_t)


# 角度

# 偏角による角ABCの求め方
# 点A(x1, y1), 点B(x2, y2), 点C(x3, y3)があるとき
# 点Bを原点とみなした点A,Cの偏角をt1,t2とすると
ABC = min(abs(t1 - t2), 360 - abs(t1 - t2))
# 偏角tは
import math

t = math.atan2(y, x) * 180 / math.pi
