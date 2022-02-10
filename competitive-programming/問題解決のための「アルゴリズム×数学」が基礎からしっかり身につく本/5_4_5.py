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
#    print("bin(i)[2:].zfill(k), mask, picked, lcm_v, num, len(picked), acc")
#    print(bin(i)[2:].zfill(k), mask, picked, lcm_v, num, len(picked), acc)


print(acc)
