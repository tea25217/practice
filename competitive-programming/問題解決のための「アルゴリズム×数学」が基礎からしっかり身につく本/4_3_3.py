L = 1
R = 2
repeat = 20

for i in range(repeat):
    m = (L + R) / 2
    if m ** 2 < 2:
        L = m
    else:
        R = m
    print(i + 1, m)
