x, y = map(int, input().split())

if x == y:
    print(x)
else:
    if x + y == 3:
        print(0)
    elif x + y == 2:
        print(1)
    else:
        print(2)
