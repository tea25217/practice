n = int(input())
a = list(map(int, input().split()))

b = list(range(1, n + 1))

if set(a) != set(b):
    print('No')
else:
    print('Yes')
