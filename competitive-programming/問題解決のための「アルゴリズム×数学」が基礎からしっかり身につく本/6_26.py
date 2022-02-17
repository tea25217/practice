from typing import List
from copy import deepcopy
from dataclasses import dataclass


@dataclass
class Matrix:
    p: List[List[float]]


def multiplication(A: Matrix, B: Matrix) -> Matrix:
    """行列A, Bの掛け算
    Args:
        A[Matrix]: 左側の行列
        B[Matrix]: 右側の行列
    Returns:
        [Matrix]: A, Bの積
    """
    A_Row = len(A.p)
    A_Col = len(A.p[0])
    B_Row = len(B.p)
    B_Col = len(B.p[0])
    assert A_Col == B_Row
    C = Matrix([[0 for j in range(B_Col)] for i in range(A_Row)])
    for i in range(A_Row):
        for j in range(B_Col):
            for k in range(A_Col):
                C.p[i][j] += A.p[i][k] * B.p[k][j]
#                C.p[i][j] %= M     # MODを取る問題の時はコメントアウトから戻す

    return deepcopy(C)


def power(A: Matrix, t: int) -> Matrix:
    """行列Aのt乗を繰り返し二乗法で計算する
    Args:
        A[Matrix]: 行列
        t:[int]: 指数
    Returns:
        [Maxtix]: Aのt乗
    """
    P = deepcopy(A)
    Matrix_Size = len(A.p)
    if t == 0:
        return Matrix([[1 if i == j else 0 for j in range(Matrix_Size)] for i in range(Matrix_Size)])
    Q = Matrix([[0 for j in range(Matrix_Size)] for i in range(Matrix_Size)])
    flag = False
    for i in range(len(bin(t))):
        if (t & (1 << i)):
            if not flag:
                Q = deepcopy(P)
                flag = True
            else:
                Q = multiplication(Q, P)
        P = multiplication(P, P)
    return deepcopy(Q)


for _ in range(int(input())):
    x, y, z, t = map(float, input().split())
    t = int(t)
    A = power(Matrix([[1 - x, y, 0], [0, 1 - y, z], [x, 0, 1 - z]]), t)
    at = sum(A.p[0])
    bt = sum(A.p[1])
    ct = sum(A.p[2])
    print(f'{at:.15f} {bt:.15f} {ct:.15f}')
