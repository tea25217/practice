n, q = map(int, input().split())
a = list(map(int, input().split()))
shift = 0


def t1():
    idxX = (x - shift) % n
    idxY = (y - shift) % n
    a[idxX - 1], a[idxY - 1] = a[idxY - 1], a[idxX - 1]


def t2():
    global shift
    shift += 1


def t3():
    idx = (x - shift) % n
    print(a[idx - 1])


for _ in range(q):
    t, x, y = map(int, input().split())
    if t == 1:
        t1()
    elif t == 2:
        t2()
    else:
        t3()
