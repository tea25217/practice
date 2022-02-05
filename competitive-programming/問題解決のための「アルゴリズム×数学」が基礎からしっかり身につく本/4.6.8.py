# (x+y)Cy % 1000000007を求める

x, y = map(int, input().split())
divider = 1000000007
fact = [0] * 200001
fact[0] = 1
for i in range(1, 200001):
    fact[i] = fact[i - 1] * i % divider


# 繰り返し二乗法で (a ** b) mod dividerを求める関数
def modPow(a, b, divider):
    p = a
    ans = 1
    for i in range(30):
        if b & (1 << i):
            ans *= p
            ans %= divider
        p *= p
        p %= divider
    return ans


# a ÷ b (mod divider)を返す
def division(a, b, divider):
    return a * modPow(b, divider - 2, divider) % divider


# 二項係数 n! / (r! - (n-r)!)
def nCr(n, r):
    return division(fact[n], fact[r] * fact[n - r] % divider, divider)


print(nCr(x + y, y))
