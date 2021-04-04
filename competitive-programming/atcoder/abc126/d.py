from collections import deque

n = int(input())
adjacency_list = [[] for i in range(n)]

for i in range(n - 1):
    u, v, w = map(int, input().split())
    adjacency_list[u - 1].append([v - 1, w])
    adjacency_list[v - 1].append([u - 1, w])

colors = [-1] * n

stack = deque([(0, 0)])

while stack:
    current, color_to_paint = stack.pop()
    colors[current] = color_to_paint

    for target, dist in adjacency_list[current]:
        if colors[target] != -1:
            continue
        if dist % 2 == 0:
            stack.append((target, color_to_paint))
        else:
            stack.append((target, (color_to_paint + 1) % 2))


for i in range(n):
    print(colors[i])
