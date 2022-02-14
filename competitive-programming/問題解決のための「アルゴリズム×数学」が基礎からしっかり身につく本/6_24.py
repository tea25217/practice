# 座標(A, B)から任意の無限遠点へ行くまでに交差する辺の数が
# 奇数：図形の中から外へ出る
# 偶数：図形の外から中へ入ってまた外へ出る
# で判定可能

n = int(input())
verticals = [list(map(int, input().split())) for i in range(n)]
dot = list(map(int, input().split()))


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


# edgeBが真ん中で、両側に位置してほしいedgeAとedgeCとのcrossが別符号か
def hasDifferentSign(edgeA, edgeB, edgeC):
    if cross(edgeB, edgeA) * cross(edgeB, edgeC) < 0:
        return True
    else:
        return False


def toEdge(dotA, dotB):
    return [dotB[0] - dotA[0], dotB[1] - dotA[1]]


# 線分(dotA, dotB)と線分(dotC, dotD)の交差判定
def isCrossing(dotA, dotB, dotC, dotD):
    result1 = hasDifferentSign(toEdge(dotA, dotD), toEdge(dotA, dotB), toEdge(dotA, dotC))
    result2 = hasDifferentSign(toEdge(dotC, dotA), toEdge(dotC, dotD), toEdge(dotC, dotB))
    return result1 and result2


atInfinity = [10 ** 9 + 1, 0]
acc = 0

for i in range(n - 1):
    if isCrossing(verticals[i], verticals[i + 1], atInfinity, dot):
        acc += 1

if isCrossing(verticals[n - 1], verticals[0], atInfinity, dot):
    acc += 1

if acc % 2 == 1:
    print("INSIDE")
else:
    print("OUTSIDE")
