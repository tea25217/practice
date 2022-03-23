import numpy as np


n, k = input().split()
k = int(k)

for i in range(k):
    n10 = int(n, 8)
    n9 = np.base_repr(n10, base=9)
    n = n9.replace('8', '5')

print(n)
