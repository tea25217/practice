n, q = map(int, input().split())
s = input()
diff = 0

for i in range(q):
    t, x = map(int, input().split())

    if t == 1:
        diff += x
        diff %= n

    if t == 2:
        x -= diff + 1
        if x < 0:
            x += n

        print(s[x])
