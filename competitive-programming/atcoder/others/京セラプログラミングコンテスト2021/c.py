from scipy.special import comb

n = int(input())
a = list(sorted(list(map(int, input().split()))))

backet = [0] * 200

for i in a:
    backet[i % 200] += 1

cnt = 0

for i in range(200):
    nn = backet[i]
    if nn < 2:
        continue
    cnt += comb(nn, 2, exact=True)

print(cnt)
