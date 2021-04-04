m = int(input())
constellation = [list(map(int, input().split())) for _ in range(m)]
n = int(input())
asterism = [list(map(int, input().split())) for _ in range(n)]

constellation.sort()
asterism.sort()
table = dict()

for i in range(n):
    h = 'x' + str(asterism[i][0]) + 'y' + str(asterism[i][1])
    table[h] = True

x_origin, y_origin = constellation[0][0], constellation[0][1]

for i in range(n):
    dx, dy = asterism[i][0] - x_origin, asterism[i][1] - y_origin

    for j in range(1, m):
        x, y = constellation[j][0] + dx, constellation[j][1] + dy
        hh = 'x' + str(x) + 'y' + str(y)
        if hh not in table:
            break
    else:
        print(dx, dy)
        exit()
