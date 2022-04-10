n = int(input())
s = [""] * n
t = [""] * n
for i in range(n):
    s[i], t[i] = input().split()

for i in range(n):
    f = False

    for a in (s[i], t[i]):
        for j in range(n):
            if i == j:
                continue
            if a == s[j] or a == t[j]:
                break
        else:
            f = True
    if not f:
        print("No")
        exit()

print("Yes")
