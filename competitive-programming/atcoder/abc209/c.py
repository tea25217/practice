n = int(input())
c = list(sorted(list(map(int, input().split()))))

used = set()
acc = 1

for i in range(1, n + 1):
    if c[i - 1] < i:
        print(0)
        exit()
    acc *= (c[i - 1] - i + 1)
    acc %= 10 ** 9 + 7

print(acc)
