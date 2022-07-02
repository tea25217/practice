n = int(input())
a = [input() for i in range(n)]

directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

ans = 0

for i in range(n):
    for j in range(n):
        for d in directions:
            x = j
            y = i
            acc = a[y][x]

            for _ in range(n - 1):
                x += d[0]
                y += d[1]

                if x < 0:
                    x = n - 1
                if x == n:
                    x = 0
                if y < 0:
                    y = n - 1
                if y == n:
                    y = 0

                acc += a[y][x]

            ans = max(ans, int(acc))

print(ans)
