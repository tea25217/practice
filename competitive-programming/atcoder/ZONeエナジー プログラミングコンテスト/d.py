t = ""
r = False
for c in input():
    if c == 'R':
        r = not(r)
        continue
    if not r:
        if len(t) < 1:
            t = t + c
        else:
            if t[-1] == c:
                t = t[:len(t) - 1]
            else:
                t = t + c
    else:
        if len(t) < 1:
            t = c + t
        else:
            if t[0] == c:
                t = t[1:]
            else:
                t = c + t

if not r:
    print(t)
else:
    print(t[::-1])
