n = int(input())
a = list(map(int, input().split()))

ans = 10 ** 31

for i in range(2 ** (n - 1)):
    acc = []
    section = 0
    for j in range(n):
        section |= a[j]
        if j != n - 1:
            if ((i >> j) & 1):
                acc.append(section)
                section = 0
        else:
            acc.append(section)
    
    acc_all = 0

    for i in acc:
        acc_all ^= i

    ans = min(ans, acc_all)

print(ans)
