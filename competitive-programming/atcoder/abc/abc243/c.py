n = int(input())
persons = [""] * n
for i in range(n):
    a, b = map(int, input().split())
    persons[i] = (a, b, i)
s = input()
persons.sort()
persons.sort(key=lambda x: x[1])
y = 0
r = False

for i in range(n):
    if persons[i][1] > y:
        y = persons[i][1]
        r = False
    if r and s[persons[i][2]] == 'L':
        print("Yes")
        exit()
    if s[persons[i][2]] == 'R':
        r = True

print("No")
