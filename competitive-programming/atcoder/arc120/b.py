from collections import deque

h, w = map(int, input().split())
s = [''] * h
for i in range(h):
    s[i] = input()

seen = [[False for j in range(w)] for i in range(h)]
q = deque()
q.append((0, 0, 0))  # depth, i, j
depth = -1
acc = 1
b = False
r = False
dot = False

while q:

    d, i, j = q.popleft()
    seen[i][j] = True

    if d > depth:
        if b and r:
            print(0)
            exit()
        elif not dot:
            pass
        elif b or r:
            pass
        else:
            acc *= 2

        if i == h - 1 and j == w - 1:
            if s[i][j] == '.':
                acc *= 2
            print(acc)
            exit()

        depth = d
        b = False
        r = False
        dot = False

        if s[i][j] == 'B':
            b = True
        elif s[i][j] == 'R':
            r = True
        else:
            dot = True
        
    else:
        if s[i][j] == 'B':
            b = True
        elif s[i][j] == 'R':
            r = True
        else:
            dot = True

    if i < h - 1:
        if not seen[i + 1][j]:
            q.append((d + 1, i + 1, j))
    if j < w - 1:
        if not seen[i][j + 1]:
            q.append((d + 1, i, j + 1))
