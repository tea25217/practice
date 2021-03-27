h, w, x, y = map(int, input().split())
m = [input() for i in range(h)]

ans = 1

# up
i = x - 1
while i > 0:
    if m[i - 1][y - 1] == '#':
        break
    ans += 1
    i -= 1

# down
i = x + 1
while i <= h:
    if m[i - 1][y - 1] == '#':
        break
    ans += 1
    i += 1

# left
i = y - 1
while i > 0:
    if m[x - 1][i - 1] == '#':
        break
    ans += 1
    i -= 1

# right
i = y + 1
while i <= w:
    if m[x - 1][i - 1] == '#':
        break
    ans += 1
    i += 1

print(ans)
