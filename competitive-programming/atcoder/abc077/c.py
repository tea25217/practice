import bisect

n = int(input())
a = list(sorted(map(int, input().split())))
b = list(sorted(map(int, input().split())))
c = list(sorted(map(int, input().split())))

ans = 0

for j in b:
    x = bisect.bisect_right(a, j - 1)
    y = bisect.bisect_left(c, j + 1)
    acc = x * (n - y)
    ans += acc

print(ans)
