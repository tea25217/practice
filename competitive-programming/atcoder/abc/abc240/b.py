n = int(input())
used = set()
for i in input().split():
    if i in used:
        continue
    used.add(i)
print(len(used))
