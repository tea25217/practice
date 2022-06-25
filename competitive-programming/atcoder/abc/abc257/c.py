from bisect import bisect_left, bisect_right


n = int(input())
s = input()
w = list(map(int, input().split()))

adult = []
child = []

for i in range(n):
    if s[i] == "0":
        child.append(w[i])
    else:
        adult.append(w[i])

adult.sort()
child.sort()
ans = 0

if len(adult) == 0 or len(child) == 0:
    print(n)
    exit()

for i, x in enumerate(child):
    a = len(adult) - bisect_right(adult, x)
    c = i
    ans = max(ans, a + c)

for i, x in enumerate(adult):
    c = bisect_left(child, x)
    a = len(adult) - i
    ans = max(ans, a + c)

x_min = len(child)
ans = max(ans, x_min)
x_max = len(adult)
ans = max(ans, x_max)

print(ans)
