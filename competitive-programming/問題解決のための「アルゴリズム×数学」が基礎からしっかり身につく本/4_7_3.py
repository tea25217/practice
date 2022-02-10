from typing import List
from copy import deepcopy
from dataclasses import dataclass


@dataclass
class Matrix:
    p: List[List[int]]


M = 1000000007
Matrix_Size = 3
Matrix_Zero = Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
Bit_Digit = 60


def multiplication(A: Matrix, B: Matrix) -> Matrix:
    C = deepcopy(Matrix_Zero)
    for i in range(Matrix_Size):
        for j in range(Matrix_Size):
            for k in range(Matrix_Size):
                C.p[i][j] += A.p[i][k] * B.p[k][j]
                C.p[i][j] %= M

    return deepcopy(C)


assert multiplication(Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) \
    == Matrix([[30, 36, 42], [66, 81, 96], [102, 126, 150]])


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


assert power(Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 2) == Matrix([[30, 36, 42], [66, 81, 96], [102, 126, 150]])


def solver(n):
    A = Matrix([[1, 1, 1], [1, 0, 0], [0, 1, 0]])
    B = power(A, n - 2)

    return (B.p[1][0] * 2 + B.p[1][1] + B.p[1][2]) % M


assert solver(10) == 149
assert solver(876543210987654321) == 639479200

n = int(input())
ans = solver(n)
print(ans)
