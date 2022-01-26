n = int(input())
p = [0] * 200001
current = 0
for i in map(int, input().split()):
    p[i] = 1
    while p[current]:
        current += 1
    print(current)