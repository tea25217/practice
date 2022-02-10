# K=4の状態遷移パターンを埋めるのがめんどいからK=3だけ解く

from typing import List
from copy import deepcopy
from dataclasses import dataclass

k, n = map(int, input().split())


@dataclass
class Matrix:
    p: List[List[int]]


M = 1000000007
Matrix_Size = 2 ** k
Matrix_Zero = Matrix([[0 for j in range(Matrix_Size)] for i in range(Matrix_Size)])
Bit_Digit = len(bin(n))     # bin(n)でprefix 0bが付く


def multiplication(A: Matrix, B: Matrix) -> Matrix:
    C = deepcopy(Matrix_Zero)
    for i in range(Matrix_Size):
        for j in range(Matrix_Size):
            for k in range(Matrix_Size):
                C.p[i][j] += A.p[i][k] * B.p[k][j]
                C.p[i][j] %= M

    return deepcopy(C)


def power(A: Matrix, n: int) -> Matrix:
    P = deepcopy(A)
    Q = deepcopy(Matrix_Zero)
    flag = False
    for i in range(Bit_Digit):
        if (n & (1 << i)):
            if not flag:
                Q = deepcopy(P)
                flag = True
            else:
                Q = multiplication(Q, P)
        P = multiplication(P, P)
    return deepcopy(Q)


def solver(n):
    A = Matrix([[0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 1, 0, 0, 1, 0]])
    B = power(A, n)

    return (B.p[Matrix_Size - 1][Matrix_Size - 1]) % M


assert solver(8) == 153

ans = solver(n)
print(ans)
