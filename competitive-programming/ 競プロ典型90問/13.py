from copy import deepcopy
from typing import List, Tuple
import heapq


def dijkstra1(adj: List[List[Tuple[int, int]]], n: int, start: int) -> List[int]:
    """ Dijkstra's algorithm

    Calc shortest path of weighted graph by Dijkstra's algorithm.
    Return cost list to all node from start node.

    Args:
        adj (List[List[Tuple[int, int]]]):
            Adjacency list.
            adj[node] = [(adjacent node num, cost)]

            Example.
            adj: [[], [(2, 10), (3, 15), (4, 20)], [(1, 10)], [(1, 20)], []]

            Node 1 has edges for node 2, 3, and 4.
            Cost for node 3 is 15.

        n (int): num of nodes
        start (int): start node

    Returns:
        List[int]: reach cost of nodes

    Precondition:
        Node number is 1-indexed.
        All list[0] is unused.
    """
    costList = [float('inf')] * (n + 1)
    costList[start] = 0
    Q = [(0, start)]    # cost for current node, node, path
    heapq.heapify(Q)

    while Q:
        currentCost, currentNode = heapq.heappop(Q)

        if currentCost > costList[currentNode]:
            continue

        for node, cost in adj[currentNode]:
            if costList[node] > currentCost + cost:
                costList[node] = currentCost + cost
                heapq.heappush(Q, (costList[node], node))

    return (deepcopy(costList))


n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

listA = dijkstra1(adj, n, 1)
listB = dijkstra1(adj, n, n)

for i in range(1, n + 1):
    print(listA[i] + listB[i])
