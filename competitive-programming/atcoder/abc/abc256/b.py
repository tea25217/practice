n = int(input())
a = list(map(int, input().split()))
p = 0

first = second = third = False

for i in range(n):
    ruida = a[i]

    if third:
        if ruida >= 1:
            p += 1
            third = False
    if second:
        if ruida >= 2:
            p += 1
            second = False
        elif ruida == 1:
            third = True
            second = False
    if first:
        if ruida >= 3:
            p += 1
            first = False
        elif ruida > 0:
            if ruida == 2:
                third = True
            else:
                second = True
            first = False

    if ruida == 4:
        p += 1
    if ruida == 3:
        third = True
    if ruida == 2:
        second = True
    if ruida == 1:
        first = True

print(p)
