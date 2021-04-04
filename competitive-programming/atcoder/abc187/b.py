n = int(input())
x = [0] * n
y = [0] * n
for i in range(n):
    xi, yi = map(int, input().split())
    x[i] = xi
    y[i] = yi

cnt = 0

for i in range(n):
    for j in range(i + 1, n):
        ix = x[i]
        iy = y[i]
        jx = x[j]
        jy = y[j]

        if (ix < 0) or (jx < 0):
            offset = abs(min(ix, jx))
            ix += offset
            jx += offset

        a = (jy - iy) / (jx - ix)

        if (a >= -1) and (a <= 1):
            cnt += 1

print(cnt)
