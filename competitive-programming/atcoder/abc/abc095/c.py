a, b, c, x, y = map(int, input().split())
ans = 10 ** 9

for i in range(max(x, y) * 2 + 1):
    comb_ab = int(i / 2 if (i % 2) == 0 else (i - 1) / 2)
    na = max(0, x - comb_ab)
    nb = max(0, y - comb_ab)
    nc = i
    cost = na * a + nb * b + nc * c
    ans = min(ans, cost)

print(ans)
