n, k = map(int, input().split())
pos = k
f = [(-1, -1)] * n

for i in range(n):
    a, b = map(int, input().split())
    f[i] = (a, b)

f.sort()

for i in range(n):
    a, b = f[i]
    if pos >= a:
        pos += b

print(pos)
