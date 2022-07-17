n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
person = [""] * n
ans = []

for i, e in enumerate(zip(a, b)):
    person[i] = (i + 1, e[0], e[1], e[0] + e[1])

person.sort(reverse=True)
person.sort(key=lambda x: x[1])

for _ in range(x):
    i, _, _, _ = person.pop(-1)
    ans.append(i)

person.sort(reverse=True)
person.sort(key=lambda x: x[2])

for _ in range(y):
    i, _, _, _ = person.pop(-1)
    ans.append(i)

person.sort(reverse=True)
person.sort(key=lambda x: x[3])

for _ in range(z):
    i, _, _, _ = person.pop(-1)
    ans.append(i)

ans.sort()
for a in ans:
    print(a)
