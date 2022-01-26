n = int(input())

ans = 0


def count_divisor(n):
    acc = 0
    for i in range(1, n + 1):
        if n % i == 0:
            acc += 1
    return acc


for i in range(1, n + 1, 2):
    if count_divisor(i) == 8:
        ans += 1

print(ans)
