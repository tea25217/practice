import queue


r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
table = [input() for i in range(r)]
visited = [[False for j in range(c)] for i in range(r)]

q = queue.Queue()
q.put((sy, sx, 0))

while q:
    y, x, d = q.get()

    if y == gy and x == gx:
        break

    for dy, dx in ([(-1, 0), (0, -1), (0, 1), (1, 0)]):
        ny, nx = (y + dy, x + dx)
        if ny == 0 or ny > r or nx == 0 or nx > c:
            continue
        if table[ny - 1][nx - 1] == '#':
            continue
        if visited[ny - 1][nx - 1]:
            continue
        else:
            visited[ny - 1][nx - 1] = True
        q.put((ny, nx, d + 1))

print(d)
