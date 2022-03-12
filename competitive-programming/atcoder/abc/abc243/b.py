n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cnt1 = 0

for i, j in zip(a, b):
    if i == j:
        cnt1 += 1

cnt2 = 0
for i in a:
    for j in b:
        if i == j:
            cnt2 += 1

cnt2 -= cnt1

print(cnt1)
print(cnt2)
