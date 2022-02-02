from math import floor

x1, y1 = map(int, input().split())  # 点Aとする
x2, y2 = map(int, input().split())  # 点Bとする
x3, y3 = map(int, input().split())  # 点Cとする
x4, y4 = map(int, input().split())  # 点Dとする

# ベクトルの成分表示
AB = (x2 - x1, y2 - y1)
AC = (x3 - x1, y3 - y1)
AD = (x4 - x1, y4 - y1)
CA = (x1 - x3, y1 - y3)
CB = (x2 - x3, y2 - y3)
CD = (x4 - x3, y4 - y3)
BD = (x4 - x2, y4 - y2)
vectors = (AB, AC, AD, BD, CA, CB, CD, BD)


def size(v):
    return (v[0]**2 + v[1]**2)**0.5


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def normalize(n):
    return floor(n * 10**9)


def isSeparated(AB, CD, vectors):
    far = -1
    for v in vectors:
        far = max(far, size(v))
    if normalize(far) > normalize(size(AB) + size(CD)):
        return True
    else:
        return False


# crossがすべて0の場合、直線上に位置する
if cross(AB, AD) == 0 and \
    cross(AB, AC) == 0 and \
    cross(CD, CA) == 0 and \
    cross(CD, CB) == 0:
    if isSeparated(AB, CD, vectors):
        print('No')
    else:
        print('Yes')
    exit()

# cross(AB, AD)とcross(AB, AC)の符号が異なるか0を含む、かつ
# cross(CD, CA)とcross(CD, CB)の符号が異なるか0を含む
# => 交差する
if cross(AB, AD) * cross(AB, AC) <= 0 and \
    cross(CD, CA) * cross(CD, CB) <= 0:
    print('Yes')
else:
    print('No')
