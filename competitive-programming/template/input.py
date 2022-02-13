# hoge
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


# メモ化再帰
# @lru_cacheをつけるだけ
from functools import lru_cache


@lru_cache
def hoge(x):
    return hoge(x)


