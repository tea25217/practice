from typing import List
from copy import deepcopy
from dataclasses import dataclass

M = 1000000007


@dataclass
class Matrix:
    p: List[List[int]]


def multiplication(A: Matrix, B: Matrix) -> Matrix:
    C = Matrix([[0, 0], [0, 0]])    # 都度deepcopyしないといけないから、切り出さず直書きの方がすっきりする
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C.p[i][j] += A.p[i][k] * B.p[k][j]
                C.p[i][j] %= M

    return deepcopy(C)


def power(A: Matrix, n: int) -> Matrix:
    P = deepcopy(A)
    Q = Matrix([[0, 0], [0, 0]])
    flag = False
    for i in range(60):
        if (n & (1 << i)):
            if not flag:
                Q = deepcopy(P)
                flag = True
            else:
                Q = multiplication(Q, P)
        P = multiplication(P, P)
    return deepcopy(Q)


n = int(input())
A = Matrix([[2, 1], [1, 0]])
B = power(A, n - 1)

ans = (B.p[1][0] + B.p[1][1]) % M

print(ans)
