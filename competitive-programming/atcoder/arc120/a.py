n = int(input())
a = list(map(int, input().split()))
dp1 = [0] * (n + 1)
dp2 = [0] * (n + 1)
max_table = [0] * (n + 1)

for i in range(1, n + 1):
    dp1[i] = dp1[i - 1] + a[i - 1]
    dp2[i] = dp2[i - 1] + dp1[i]
    max_table[i] = max(max_table[i - 1], a[i - 1])

for i in range(1, n + 1):
    print(dp2[i] + max_table[i] * i)
