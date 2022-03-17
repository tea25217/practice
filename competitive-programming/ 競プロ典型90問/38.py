import numpy as np


a, b = map(int, input().split())
g = np.gcd(a, b)
ans = a * b // g

if ans > 10 ** 18:
    print("Large")
else:
    print(ans)
