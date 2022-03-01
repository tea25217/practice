from typing import Any, Callable, Generator, List


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

        Example:

        Apply to [2, 5)

        Array
        [0][1][2 ][3 ][4 ][5 ][6 ][7 ]

        Apply targets
        [*][*][2 ][3 ][4 ][* ][* ][* ]

        Segment Tree
        [            1            ]
        [      2     ][     3     ]
        [  4  ][  5  ][  6  ][  7  ]
        [8][9][10][11][12][13][14][15]

        Apply targets
        [            *            ]
        [      *     ][     *     ]
        [  *  ][  5  ][  *  ][  *  ]
        [*][*][* ][* ][12][* ][* ][* ]

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


class LazySegTree(SegTree):
    """Lazy Propagation Segment Tree

    *** CAUTION ***
    This class is template.
    Use LazySegTreeRUQ or LazySegTreeRUQ.

    Args:
        SegTree (class): super class
    """
    def _getPropagationIndexes(self, L: int, R: int) -> Generator[int, None, None]:
        """generate indexes for lazy propagation

        Example:

        Query to [2, 5)

        Array
        [0][1][2 ][3 ][4 ][5 ][6 ][7 ]

        Query targets
        [*][*][2 ][3 ][4 ][* ][* ][* ]

        Segment Tree
        [            1            ]
        [      2     ][     3     ]
        [  4  ][  5  ][  6  ][  7  ]
        [8][9][10][11][12][13][14][15]

        Propagation method targets
        [            1            ]
        [      2     ][     3     ]
        [  *  ][  5  ][  6  ][  *  ]

        Args:
            L (int): left index (0-index)
            R (int): right index (0-index)

        Yields:
            Generator[int, None, None]: indexes of lazy evaluation targets
        """
        L += self.leavesSize
        R += self.leavesSize - 1
        overlap = True if L == R else False
        for i in range(self.height):
            L >>= 1
            R >>= 1
            if not overlap and L == R:
                overlap = True
            if not overlap:
                for j in range(L + 1, R):
                    yield j
                yield R
            yield L

    def _propagate(self, L: int, R: int) -> None:
        """lazy propagation

        Args:
            L (int): left index (0-index)
            R (int): right index (0-index)
        """
        ...

    def _eval(self, L: int, R: int) -> None:
        """lazy evaluation

        Args:
            L (int): left index (0-index)
            R (int): right index (0-index)
        """
        ...


class LazySegTreeRUQ(LazySegTree):
    """Lazy Propagation Segment Tree(RUQ)

    * Range Update

    Args:
        LazySegTree (class): super class
    Attributes:
        lazy(List[any]): for lazy evaluation (1-index)
    """
    def __init__(self, n: int, f: Callable, e: Any, initialValues: List[Any] = []) -> None:
        super().__init__(n, f, e, initialValues)
        self.lazy = [e] * 2 * self.leavesSize

    def _propagate(self, L: int, R: int) -> None:
        for i in reversed(list(self._getPropagationIndexes(L, R))):
            v = self.lazy[i]
            if v == self.e:
                continue
            self.tree[i] = self.lazy[2 * i] = self.lazy[2 * i + 1] = v
            self.lazy[i] = self.e

    def _eval(self, L: int, R: int) -> None:
        self._propagate(L, R)
        for i in range(L + self.leavesSize, R + self.leavesSize):
            self.tree[i] = self.f(self.tree[i], self.lazy[i])
            self.lazy[i] = self.e

    def update(self, L: int, R: int, n: Any) -> None:
        """range update [L, R)

        Args:
            L (int): left index (0-index)
            R (int): right index (0-index)
            n (Any): new value
        """
        self._eval(L, R)
        *indexes, = self._getPropagationIndexes(L, R)
        L += self.leavesSize
        R += self.leavesSize

        while L < R:
            if L & 1:
                self.lazy[L] = self.tree[L] = n
                L += 1
            if R & 1:
                R -= 1
                self.lazy[R] = self.tree[R] = n
            L >>= 1
            R >>= 1

        for i in indexes:
            self.tree[i] = self.f(self.tree[i * 2], self.tree[i * 2 + 1])

    def query(self, L: int, R: int) -> Any:
        self._eval(L, R)
        return super().query(L, R)


def main():
    def assertSegTree():
        def printAndAssert(tree, L, R, correct):
            print(tree.query(L, R))
            assert tree.query(L, R) == correct

        def updatePrintAndAssert(tree, upK, upX, L, R, correct):
            tree.update(upK, upX)
            printAndAssert(tree, L, R, correct)

        A = [14, 5, 9, 13, 7, 12, 11, 1, 7, 8]
        n = len(A)

        seg = SegTree(n, min, float('inf'), A)
        printAndAssert(seg, 0, 8, 1)                # min([A[0:8]) == 1 (A[7])
        updatePrintAndAssert(seg, 5, 2, 0, 8, 1)    # A[5] = 2, min([A[0:8]) == 1 (A[7])
        updatePrintAndAssert(seg, 8, 0, 0, 8, 1)    # A[8] = 0, min([A[0:8]) == 1 (A[7])
        updatePrintAndAssert(seg, 7, 3, 0, 8, 2)    # A[7] = 3, min([A[0:8]) == 2 (A[5])
        updatePrintAndAssert(seg, 7, 0, 0, 8, 0)    # A[7] = 0, min([A[0:8]) == 0 (A[7])

        seg2 = SegTree(5, max, -float('inf'))       # arr = [-float('inf')] * 5
        printAndAssert(seg2, 0, 5, -float('inf'))   # min(arr) == -float('inf')
        updatePrintAndAssert(seg2, 4, 0, 0, 5, 0)   # arr[4] == 0, max(arr) == 0 (arr[4])
        updatePrintAndAssert(seg2, 0, 1, 0, 5, 1)   # arr[0] == 1, max(arr) == 1 (arr[0])

    def assertLazySegTreeRUQ():
        def printLazyTreeInfo(tree):
            print(f"tree: {tree.tree}")
            print(f"lazy: {tree.lazy}")
            print(f"leaves: {tree.tree[tree.leavesSize:]}")

        segRUQ = LazySegTreeRUQ(5, max, -float('inf'))
        segRUQ.update(0, 5, 1)
        print("***** update [0, 5) +1")
        printLazyTreeInfo(segRUQ)
        print(segRUQ.query(0, 5))
        print("***** query [0, 5)")
        printLazyTreeInfo(segRUQ)
        segRUQ.update(2, 3, 2)
        print("***** update [2, 3) +2")
        printLazyTreeInfo(segRUQ)
        print(segRUQ.query(0, 5))
        print("***** query [0, 5)")
        printLazyTreeInfo(segRUQ)

if __name__ == '__main__':
    main()


# References
#
# Pythonでアルゴリズム（セグメント木）（実践）
# https://qiita.com/takayg1/items/c811bd07c21923d7ec69
#
# セグメント木を徹底解説！0から遅延評価やモノイドまで | アルゴリズムロジック
# https://algo-logic.info/segment-tree/
#
# 遅延評価セグメント木をソラで書きたいあなたに - hogecoder
# https://tsutaj.hatenablog.com/entry/2017/03/30/224339
#
# RMQ and RUQ (遅延評価セグメント木) - yaketake08's 実装メモ
# https://tjkendev.github.io/procon-library/python/range_query/rmq_ruq_segment_tree_lp.html
#
