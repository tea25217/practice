class UnionFind():
    def __init__(self, n: int) -> None:
        self.n = n
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, x: int) -> int:
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x: int, y: int) -> None:
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
        return self.find(x) == self.find(y)
