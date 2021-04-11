n = input()

cnt = 0
for c in n[::-1]:
    if c != '0':
        break
    else:
        cnt += 1

n = n[:len(n) - cnt]

if n == n[::-1]:
    print("Yes")
else:
    print("No")
