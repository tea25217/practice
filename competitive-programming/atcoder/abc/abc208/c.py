n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(sorted(a))

a1 = k // n
dash = b[k % n]

for i in a:
    if i < dash:
        print(a1 + 1)
    else:
        print(a1)
