# This file has following functions.
#
# dijkstra1: Returns cost list
# dijkstra2: Returns cost list and shortest path list[str]
# (Heavy memory required)
# dijkstra3: Returns cost list and shortest path list[list[int]]
# (Heavy time and memory required)

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


def dijkstra2(adj: List[List[Tuple[int, int]]], n: int, start: int) -> Tuple[List[int], List[str]]:
    """ Dijkstra's algorithm

    Calc shortest path of weighted graph by Dijkstra's algorithm.
    Return cost list and shortest path list to all node from start node.

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
        Tuple[List[int], List[List[int]]]:
            List[int]: reach cost of nodes
            List[str]:
                Shortest path of nodes.

                Example.
                ["", "", ",1", ",1,2,4", ",1,2"]

                Start is 1.
                To node 2, shortest path is 1-2.
                To node 3, shortest path is 1-2-4-3.
                To node 4, shortest path is 1-2-3.

    Precondition:
        Node number is 1-indexed.
        All list[0] is unused.
    """
    costList = [float('inf')] * (n + 1)
    costList[start] = 0
    pathList = [''] * (n + 1)
    Q = [(0, start, '')]    # cost for current node, node, path
    heapq.heapify(Q)

    while Q:
        currentCost, currentNode, path = heapq.heappop(Q)

        if currentCost > costList[currentNode]:
            continue

        path += ',' + str(currentNode)

        for node, cost in adj[currentNode]:
            if costList[node] > currentCost + cost:
                costList[node] = currentCost + cost
                pathList[node] = path
                heapq.heappush(Q, (costList[node], node, path))

    return (deepcopy(costList), deepcopy(pathList))


def dijkstra3(adj: List[List[Tuple[int, int]]], n: int, start: int) -> Tuple[List[int], List[List[int]]]:
    """ Dijkstra's algorithm

    Calc shortest path of weighted graph by Dijkstra's algorithm.
    Return cost list and shortest path list to all node from start node.

    Args:
        adj (List[List[Tuple[int, int]]]):
            Adjacency list.
            adj[node] = [(adjacent node num, cost)]

            Example.
            adj: [[], [(2, 10), (3, 15), (4, 20)], [(1, 10)], [(1, 20)], []]

            node 1 has edges for node 2, 3, and 4.
            cost for node 3 is 15.

        n (int): num of nodes
        start (int): start node

    Returns:
        Tuple[List[int], List[List[int]]]:
            List[int]: reach cost of nodes
            List[List[int]]: shortest path of nodes

    Precondition:
        Node number is 1-indexed.
        All list[0] is unused.
    """
    costList = [float('inf')] * (n + 1)
    costList[start] = 0
    pathList = [[] for i in range(n + 1)]
    Q = [(0, start, [])]    # cost for current node, node, path
    heapq.heapify(Q)

    while Q:
        currentCost, currentNode, path = heapq.heappop(Q)

        if currentCost > costList[currentNode]:
            continue

        path.append(currentNode)

        for node, cost in adj[currentNode]:
            if costList[node] > currentCost + cost:
                costList[node] = currentCost + cost
                pathList[node] = deepcopy(path)
                heapq.heappush(Q, (costList[node], node, deepcopy(path)))

    return (deepcopy(costList), deepcopy(pathList))


# AOL GRL_1_A
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=ja
v, e, r = map(int, input().split())
adjacency_list = [[] for i in range(v + 1)]
r += 1

for i in range(e):
    s, t, d = map(int, input().split())
    s += 1
    t += 1
    adjacency_list[s].append((t, d))

costList = dijkstra1(adjacency_list, v, r)
for i in range(1, v + 1):
    if costList[i] == float('inf'):
        print("INF")
    else:
        print(costList[i])
