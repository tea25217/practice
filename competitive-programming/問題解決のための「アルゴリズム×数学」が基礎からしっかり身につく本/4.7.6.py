from copy import deepcopy
from dataclasses import dataclass

Billion = 10 ** 9
Matrix_Zero = [[0, 0], [0, 0]]


@dataclass
class Matrix:
    p: list[list[int]]


def multiplication(A: Matrix, B: Matrix) -> Matrix:
    C = Matrix(Matrix_Zero)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C.p[i][j] += A.p[i][k] * B.p[k][j]
                C.p[i][j] %= Billion

    return deepcopy(C)


def power(A: Matrix, n: int) -> Matrix:
    P = deepcopy(A)
    Q = Matrix(Matrix_Zero)
    flag = False
    for i in range(60):
        if (n & (1 << i)):
            if not flag:
                Q = deepcopy(P)
                flag = True
            else:
                Q = multiplication(Q, P)
        P = multiplication(P, P)
        print(i, Q)
    return deepcopy(Q)


n = 4   # int(input())
A = Matrix([[1, 1], [1, 0]])
B = power(A, n - 1)

ans = (B.p[1][0] + B.p[1][1]) % Billion

print(ans)
