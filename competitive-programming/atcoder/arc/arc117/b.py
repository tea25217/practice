n = int(input())
a = list(sorted(list(map(int, input().split()))))

acc = 1
acc *= a[0] + 1

for i in range(1, n):
    acc *= (a[i] - a[i - 1]) + 1

acc %= 10 ** 9 + 7

print(acc)
