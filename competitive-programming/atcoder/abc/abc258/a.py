k = int(input())
h = str(21 + k // 60)
m = str(k % 60).zfill(2)
print(h + ":" + m)
