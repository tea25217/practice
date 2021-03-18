from collections import deque

h, w = map(int, input().split())
c = [input() for _ in range(h)]

for i, letters in enumerate(c):
    for j, letter in enumerate(letters):
        if letter == "s":
            s_i = i
            s_j = j

stack = deque([(s_i, s_j)])
visited = [[False] * w for _ in range(h)]

while stack:
    row, col = stack.pop()
#    print(row, col)

    if (row < 0) or (row >= h) or (col < 0) or (col >= w):
#        print("out of town")
        continue

    if visited[row][col]:
#        print("visited")
        continue
    else:
        visited[row][col] = True

    if c[row][col] == "g":
        print("Yes")
        exit()

    if c[row][col] == "#":
#        print("fence")
        continue

    for i, j in ([1, 0], [-1, 0], [0, 1], [0, -1]):
        stack.append((row + i, col + j))
#        print("append")

print("No")
