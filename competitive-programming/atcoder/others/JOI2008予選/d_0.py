# バグが取れないので捨てる

import bisect

m = int(input())
constellation = [list(map(int, input().split())) for _ in range(m)]
n = int(input())
asterism = [list(map(int, input().split())) for _ in range(n)]

constellation.sort()
asterism.sort()
asterism_x = [i[0] for i in asterism]

x_origin, y_origin = constellation[0][0], constellation[0][1]

dist = []
for i in range(m):
    dx, dy = constellation[i][0] - x_origin, constellation[i][1] - y_origin
    dist.append((dx, dy))


def isIncludeTheStar(ix):
    while ix < n and asterism[ix][0] == x + dx:
        if y + dy == asterism[ix][1]:
            return True
        ix += 1
    else:
        return False


for i in range(n):
    x, y = asterism[i][0] - x_origin, asterism[i][1] - y_origin

    for j in range(1, m):
        dx, dy = dist[j][0], dist[j][1]
        ix = bisect.bisect_left(asterism_x, x + dx)

        if not isIncludeTheStar(ix):
            break
    else:
        print(x, y)
        exit()
