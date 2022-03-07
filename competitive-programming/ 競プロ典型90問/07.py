from bisect import bisect_left


n = int(input())
a = sorted(list(map(int, input().split())))
q = int(input())
for _ in range(q):
    b = int(input())
    idx = bisect_left(a, b)
    ans = 10 ** 9
    if idx < n:
        ans = min(ans, abs(b - a[idx]))
    if idx > 0:
        ans = min(ans, abs(b - a[idx - 1]))
    print(ans)
