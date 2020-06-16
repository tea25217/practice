import numpy as np

x, n = map(int, input().split())
arr = {i for i in range(102)}

for i in input().split():
    arr.remove(int(i))

arr = list(arr)

idx = np.abs(np.asarray(arr) - x).argmin()

print(arr[idx])