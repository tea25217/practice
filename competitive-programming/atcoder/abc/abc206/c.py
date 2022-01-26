import bisect

n = int(input())
a = list(sorted(list(map(int, input().split()))))
acc = 0

for i in a:
    left = bisect.bisect_left(a, i)
    right = bisect.bisect_right(a, i)
    acc += left + (n - right)

print(acc//2)
