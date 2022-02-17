from sys import setrecursionlimit


setrecursionlimit(100000)

n = int(input())
adj = [[] for i in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)


def dfs(x, parent):
    """
    Args:
        x[int]: current node
        parent[int]: parent node

    Returns:
        [int, int]: childlen count, answer count of children
    """
    if len(adj[x]) == 1 and adj[x][0] == parent:
        return (1, 0)
    childlen = 1
    acc = 0

    for i in adj[x]:
        if i == parent:
            continue
        c, childAcc = dfs(i, x)
        childlen += c
        acc += childAcc
        acc += c * (n - c)

    return (childlen, acc)


print(dfs(1, 0)[1])
