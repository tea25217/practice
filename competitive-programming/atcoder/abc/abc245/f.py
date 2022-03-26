from sys import setrecursionlimit
from collections import deque
from copy import deepcopy
from typing import List
setrecursionlimit(10 ** 9)


def scc(adj: List[List[int]], rAdj: List[List[int]], n: int) -> List[List[int]]:
    """ Strongly Connected Component

    Args:
        adj (List[List[int]]): adjacent node list
        rAdj (List[List[int]]): reversed adjacent node list
        n (int): number of nodes

    Returns:
        List[List[int]]: list of Strongly Connected Components
    """
    seen = [False] * (n + 1)
    stack = deque([])

    def _dfs1(n):
        if not adj[n]:
            return n
        for i in adj[n]:
            if seen[i]:
                continue
            seen[i] = True
            stack.append(_dfs1(i))
        return n

    for i in range(1, n + 1):
        if not seen[i]:
            seen[i] = True
            stack.append(_dfs1(i))

    seen = [False] * (n + 1)
    q = deque([])
    scc = []

    while stack:
        node = stack.pop()
        if not seen[node]:
            seen[node] = True
            q.append(node)
            scc.append([])

        while q:
            c = q.popleft()
            for i in rAdj[c]:
                if seen[i]:
                    continue
                seen[i] = True
                q.append(i)
            scc[-1].append(c)

    return deepcopy(scc)


def main():
    n, m = map(int, input().split())
    adj1 = [[] for i in range(n + 1)]
    adj2 = [[] for i in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj1[a].append(b)
        adj2[b].append(a)

    sccList = scc(adj1, adj2, n)

    dp = [False] * len(sccList)
    group = [-1] * (n + 1)
    for i in range(len(sccList)):
        for j in sccList[i]:
            group[j] = i

    ans = 0
    for i in range(len(sccList) - 1, -1, -1):
        if len(sccList[i]) == 1:
            for e in adj1[sccList[i][0]]:
                dp[i] |= dp[group[e]]
        else:
            dp[i] = True

        if dp[i]:
            ans += len(sccList[i])

    print(ans)


main()
