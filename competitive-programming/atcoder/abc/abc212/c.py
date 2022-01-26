import bisect

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(sorted(list(map(int, input().split()))))

ans = 10 ** 10

for i in a:
    l = bisect.bisect_left(b, i)
    if l > 0:
        ans = min(ans, abs(i - b[l - 1]))
    if l < m:
        ans = min(ans, abs(i - b[l]))

print(ans)
