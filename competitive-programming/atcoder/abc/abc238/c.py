from math import floor

M = 998244353
Inv2 = 499122177    # 998244353の逆元

n = int(input())
digit_sum = [0] * 20

# 桁ごとの合計値
for i in range(1, 20):
    r = (10 ** i) - (10 ** (i - 1))
    digit_sum[i] = (r * (r + 1)) * Inv2 % M


# 前の桁までの合計値
cusum = [0] * 20
for i in range(1, 20):
    cusum[i] = (cusum[i - 1] + digit_sum[i - 1]) % M


l = len(str(n))
if l == 1:
    remain = n
else:
    remain = n - int('9' * (l - 1))
remain = (remain * (remain + 1)) * Inv2 % M

ans = floor((cusum[l] + remain) % M)

print(ans)
