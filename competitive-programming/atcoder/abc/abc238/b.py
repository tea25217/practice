n = int(input())
a = list(map(int, input().split()))

s = set()
s.add(0)
degree = 0

for i in a:
    degree = (degree + i) % 360
    s.add(degree)

s = list(sorted(list(s)))

for i, e in enumerate(s):
    if len(s) == 1:
        ans = 360
        break
    if i == 0:
        ans = e + (360 - s[-1])
    else:
        ans = max(ans, e - s[i - 1])

print(ans)
