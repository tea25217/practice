# 定数

# 素数
M = 998244353
M = 1000000007

# 逆元
Inv2 = 499122177    # mod 998244353における2の逆元
Inv2 = 500000004    # mod 1000000007における2の逆元


# mod M におけるnの逆元

# mod Mの世界では÷nを×toInverseElement(M, n)に置き換える
# 1/n = (n ** M-2 mod M)
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


# mod Mの二項係数
from math import factorial

# 一回きりの場合
def nCrModM(n, r, M):
    return (factorial[n] * toInverseElement[r] * toInverseElement[n - r]) % M

# 何度も計算する場合
# 事前計算
K = 5000   # 制約に応じて必要な最大値を設定する
fact = [factorial[i] % M for i in range(1, K + 1)]
inv = [toInverseElement(M, i) for i in range(1, K + 1)]

# nCr mod M
def nCrModM(n, r, M):
    return (fact[n] * inv[r] * inv[n - r]) % M
