n, x = map(int, input().split())
a = list(map(int, input().split()))

p = sum(a) - len(a) // 2

if x >= p:
    print('Yes')
else:
    print('No')