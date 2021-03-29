import bisect

d = int(input())
n = int(input())
m = int(input())
s = list(sorted([0 if i == 0 else int(input()) for i in range(n)]))
k = [int(input()) for i in range(m)]

acc = 0

for i in k:
    x = bisect.bisect_left(s, i)
    if x == n:
        d1 = d - i
        d2 = i - s[x - 1]
        acc += min(d1, d2)
    elif x == 0:
        continue
    else:
        d1 = s[x] - i
        d2 = i - s[x - 1]
        acc += min(d1, d2)

print(acc)
