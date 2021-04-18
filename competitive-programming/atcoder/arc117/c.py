n = int(input())
tree = [0] * (n + 1)
adjacency = [[] for i in range(n + 1)]
for i in range(1, n):
    a, b = map(int, input().split())
    adjacency[a].append(b)
    adjacency[b].append(a)


seen = [False] * (n + 1)
seen[1] = True 
# search end
def dfs1(start):
    if len(adjacency[start]) == 1:
        return start
    for i in adjacency[start]:
        if seen[i]:
            continue
        else:
            seen[i] = True
        x = dfs1(i)
        if x != 0:
            return x
    return 0


s = dfs1(1)

seen = [False] * (n + 1)
seen[s] = True
trace_tmp = []
# search root
def dfs2(s, trace):
    if len(adjacency[s]) == 1:
        global trace_tmp
        if len(trace) >= len(trace_tmp):
            trace_tmp = trace + [s]
    for i in adjacency[s]:
        if seen[i]:
            continue
        else:
            seen[i] = True
        dfs2(i, trace + [s])


dfs2(s, [])
root_i = len(trace_tmp) // 2
root = trace_tmp[root_i]
seen = [False] * (n + 1)
seen[root] = True


# make answer
def dfs3(s, depth):
    for i in adjacency[s]:
        if seen[i]:
            continue
        else:
            seen[i] = True
        tree[i] = depth + 1
        if len(adjacency[i]) == 0:
            continue
        dfs3(i, depth + 1)


tree[root] = 1
dfs3(root, 1)

for i in range(1, n + 1):
    print(tree[i], end="")
    if i < n:
        print(" ", end="")
