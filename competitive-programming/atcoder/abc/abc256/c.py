h1, h2, h3, w1, w2, w3 = map(int, input().split())
ans = 0

for a in range(1, 29):
    for b in range(1, 29):
        if a + b > 29 or a + b >= h1:
            break
        e = h1 - a - b
        for c in range(1, 29):
            for d in range(1, 29):
                if c + d > 29 or c + d >= h2:
                    break
                f = h2 - c - d

                if a + c >= w1:
                    break
                g = w1 - a - c

                if b + d >= w2:
                    break
                h = w2 - b - d

                if g + h < h3:
                    i = h3 - g - h

                    if w3 - e - f == i:
                        ans += 1

print(ans)
