a, b = input().split()
s_a = s_b = 0
keta = 3

for i in range(keta):
    s_a += int(a[i])
    s_b += int(b[i])

print(max(s_a, s_b))
