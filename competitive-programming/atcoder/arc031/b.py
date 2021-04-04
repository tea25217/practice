from copy import deepcopy
from collections import deque

country = [input() for _ in range(10)]


def dfs(land, x, y):
    
    stack = deque([(x, y)])

    while stack:

        i, j = stack.pop()
        land[i] = land[i][:j] + "x" + land[i][j + 1:]

        for next_i, next_j in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
            if (next_i < 0) or (next_i >= 10) or (next_j < 0) or (next_j >= 10):
                continue
            if land[next_i][next_j] == "x":
                continue
            
            stack.append((next_i, next_j))


def isOneIsland(reclaimed):
    flag = False

    for i in range(10):
        for j in range(10):
            if reclaimed[i][j] == "o":
                if flag:
                    return False
                else:
                    dfs(reclaimed, i, j)
                    flag = True

    return True
    

for i in range(10):
    for j in range(10):
        if country[i][j] == "o":
            continue

        reclaimed = deepcopy(country)
        reclaimed[i] = reclaimed[i][:j] + "o" + reclaimed[i][j + 1:]

        if isOneIsland(reclaimed):
            print("YES")
            exit()


print("NO")
