n = int(input())
ans = [0] * 10000

for i in range(1, 101):
    for j in range(1, 101):
        for k in range(1, 101):
            m = ((i ** 2) + (j ** 2) + (k ** 2) + (i * j) + (j * k) + (k * i))
            if m < 10001:
                ans[m-1] += 1

for i in range(n):
    print(ans[i])