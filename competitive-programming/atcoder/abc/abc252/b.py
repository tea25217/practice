n, k = map(int, input().split())
a = (list(map(int, input().split())))
b = list(map(int, input().split()))

t = max(a)
foods = []

for i in b:
    if a[i - 1] == t:
        print("Yes")
        break
else:
    print("No")
