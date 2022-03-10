# ワーストケースでTLE
# セグ木のロジックを改善するかスライド最小値でやる必要がある
from typing import Any, Callable, List


class SegTree:
    """Segment Tree

    * One point update
    * Any function

    Attributes:
        n (int): num of elements
        f (Callable): operation for intervals
        e (Any): identity element
        initialValues (List[any], optional): initial values
        leavesSize (int): num of leaves
        height (int): height of tree
        tree(List[any]): segment tree (1-index)
    """
    def __init__(self, n: int, f: Callable, e: Any, initialValues: List[Any] = []) -> None:
        self.n = n
        self.f = f
        self.e = e
        self.leavesSize = 1 << (n - 1).bit_length()
        self.height = n.bit_length()
        self.tree = [e] * 2 * self.leavesSize
        if initialValues:
            for i in range(n):
                self.tree[self.leavesSize + i] = initialValues[i]
        for i in range(self.leavesSize - 1, 0, -1):
            self.tree[i] = self.f(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k: int, x: Any) -> None:
        """update k-th value to x

        Args:
            k (int): index (0-index)
            x (Any): update value
        """
        k += self.leavesSize
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.f(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, L: int, R: int) -> Any:
        """apply f to [l, r)

        Args:
            L (int): index (0-index)
            R (int): index (0-index)

        Returns:
            Any: query response
        """
        res = self.e
        L += self.leavesSize
        R += self.leavesSize

        while L < R:
            if L & 1:
                res = self.f(res, self.tree[L])
                L += 1
            if R & 1:
                res = self.f(res, self.tree[R - 1])
            L >>= 1
            R >>= 1
        return res


w, n = map(int, input().split())
tree = SegTree(w + 1, max, -float("inf"))
tree.update(0, 0)


def solve(j):
    g = j - L + 1
    s = max(j - R, 0)
    if g > 0 and g > s:
        lastValue = tree.tree[tree.leavesSize + j]
        newValue = max(tree.query(s, g) + dish, lastValue)
        if newValue > lastValue:
            tree.update(j, newValue)


for i in range(1, n):
    L, R, dish = map(int, input().split())
    for j in range(w, L - 1, -1):
        solve(j)

L, R, dish = map(int, input().split())
solve(w)

ans = tree.tree[tree.leavesSize + w]

if ans == -float("inf"):
    print(-1)
else:
    print(ans)
