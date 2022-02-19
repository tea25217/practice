x1, y1, x2, y2 = map(int, input().split())

mv = ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2))

for dx1, dy1 in mv:
    for dx2, dy2 in mv:
        if (x1 + dx1 == x2 + dx2) and (y1 + dy1 == y2 + dy2):
            print("Yes")
            exit()
print("No")
