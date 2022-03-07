class UnionFind():
    """Union Find Tree

    Attributes:
        n (int): num of nodes
        par (list[int]): parent of nodes
        rank (list[int]): depth of connected subtrees

    """
    def __init__(self, n: int) -> None:
        self.n = n
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, x: int) -> int:
        """Find root node of x

        Args:
            x (int): node

        Returns:
            int: root node of x
        """
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x: int, y: int) -> None:
        """Connect subtrees include node x and node y

        Args:
            x (int): node
            y (int): node
        """
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        x_rank = self.rank[x_root]
        y_rank = self.rank[y_root]

        if x_rank > y_rank:
            self.par[y_root] = x_root
        else:
            self.par[x_root] = y_root
            if x_rank == y_rank:
                self.rank[y_root] += 1

    def same(self, x: int, y: int) -> bool:
        """ Node x and y are in same subtree or not

        Args:
            x (int): node
            y (int): node

        Returns:
            bool: True if x and y are in same subtree. False otherwise.
        """
        return self.find(x) == self.find(y)


h, w = map(int, input().split())
n = h * w
tree = UnionFind(n)
red = [[False for j in range(w)] for i in range(h)]


def calcNode(r, c):
    return (r - 1) * w + c


def check(ra, ca, rb, cb):
    if not red[ra - 1][ca - 1] or not red[rb - 1][cb - 1]:
        return False
    nodeA = calcNode(ra, ca)
    nodeB = calcNode(rb, cb)
    if tree.same(nodeA, nodeB):
        return True
    else:
        return False


for _ in range(int(input())):
    t, *square = map(int, input().split())
    if t == 1:
        r = square[0]
        c = square[1]
        red[r - 1][c - 1] = True
        for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            toR = r + dr
            toC = c + dc
            if toR == 0 or toR == h + 1 or toC == 0 or toC == w + 1:
                continue
            if red[toR - 1][toC - 1]:
                nodeX = calcNode(r, c)
                nodeY = calcNode(toR, toC)
                tree.unite(nodeX, nodeY)

    else:
        if check(*square):
            print("Yes")
        else:
            print("No")
