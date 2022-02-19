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
