a, b = map(int, input().split())
plus = [0] * a
minus = [0] * b

if a >= b:
    for i in range(a):
        plus[i] = i + 1
    for i in range(b):
        minus[i] -= i + 1
    acc = 0
    for i in range(b, a):
        acc -= i + 1
    minus[b - 1] += acc
else:
    for i in range(a):
        plus[i] = i + 1
    for i in range(b):
        minus[i] -= i + 1
    acc = 0
    for i in range(a, b):
        acc += i + 1
    plus[a - 1] += acc

for i in plus:
    print(i, end=" ")
for i, e in enumerate(minus):
    print(e, end="")
    if i < b - 1:
        print(" ", end="")
