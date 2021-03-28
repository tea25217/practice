from copy import deepcopy

n, m = map(int, input().split())
lamp = []
for i in range(m):
    k, *s = map(int, input().split())
    lamp.append([k, s])
p = list(map(int, input().split()))
ans = 0

for i in range(2 ** n):
    for j in range(m):
        need = deepcopy(lamp[j][1])
        acc_s = 0
        for k in range(n):
            if ((i >> k) & 1):
                if (k + 1) in need:
                    acc_s += 1
        acc_s %= 2
        if acc_s != p[j]:
            break
    else:
        ans += 1

print(ans)
