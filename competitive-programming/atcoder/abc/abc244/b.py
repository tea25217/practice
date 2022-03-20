n = int(input())
t = input()
x = y = 0
d = 0
for c in t:
    if c == 'R':
        d += 1
        d %= 4
    else:
        if d == 0:
            x += 1
        elif d == 1:
            y -= 1
        elif d == 2:
            x -= 1
        else:
            y += 1

print(x, y)
