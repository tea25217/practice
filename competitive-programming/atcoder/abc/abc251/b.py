n, w = map(int, input().split())
a = list(sorted(list(map(int, input().split()))))

nums = set()

for i in a:
    if i > w:
        break
    nums.add(i)

for i in range(n):
    for j in range(i + 1, n):
        if a[i] + a[j] > w:
            continue
        nums.add(a[i] + a[j])

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if a[i] + a[j] + a[k] > w:
                continue
            nums.add(a[i] + a[j] + a[k])

print(len(nums))
