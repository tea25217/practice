# n<=3000でTLE
# n<=500までAC
#
# 2点の組み合わせを全列挙し、
# マンハッタン距離dの大きい順（マイナスを付与）でheapqへ追加
# 先頭要素のdが同じ間、要素を取り出してリスト化
# リスト内で正方形を作れればbreakしサイズを出力

import heapq

n = int(input())
poll = [list(map(int, input().split())) for _ in range(n)]
dist = []
heapq.heapify(dist)
ans = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        ix, iy, jx, jy = poll[i][0], poll[i][1], poll[j][0], poll[j][1]
        d = -(abs(ix - jx) + abs(iy - jy))
        heapq.heappush(dist, (d, i, j))


def isAtRightAngles(edge1, edge2):
    if edge1[1] == edge2[1]:
        a, b, c = edge1[2], edge1[1], edge2[2]
    elif edge1[2] == edge2[1]:
        a, b, c = edge1[1], edge1[2], edge2[2]
    elif edge1[1] == edge2[2]:
        a, b, c = edge1[2], edge1[1], edge2[1]
    else:
        a, b, c = edge1[1], edge1[2], edge2[1]

    pa, pb, pc = poll[a], poll[b], poll[c]
    pax, pay, pbx, pby, pcx, pcy = pa[0], pa[1], pb[0], pb[1], pc[0], pc[1]
    dxab = pbx - pax
    dybc = pcy - pby
    dyab = pby - pay
    dxbc = pcx - pbx
    if (dxab == -dybc) and (dyab == dxbc) or (dxab == dybc) and (dyab == -dxbc):
        return True
    else:
        return False


def calcLength(edge):
    a, b = edge[1], edge[2]
    ax, ay, bx, by = poll[a][0], poll[a][1], poll[b][0], poll[b][1]
    x = abs(ax - bx)
    y = abs(ay - by)
    if x == 0:
        return y
    if y == 0:
        return x
    return (x ** 2 + y ** 2) ** 0.5


while dist:
    if ans > 0:
        break
    d = dist[0][0]
    edge = []
    while dist and dist[0][0] == d:
        edge.append(heapq.heappop(dist))

    if len(edge) >= 4:
        for i in edge:
            if ans > 0:
                break
            for j in edge:
                if ans > 0:
                    break
                if i == j:
                    continue
                if (i[1] not in [j[1], j[2]]) and (i[2] not in [j[1], j[2]]):
                    continue
                if not isAtRightAngles(i, j):
                    continue

                for k in edge:
                    if ans > 0:
                        break
                    if i == k or j == k:
                        continue
                    if (k[1] not in [j[1], j[2]]) and (k[2] not in [j[1], j[2]]):
                        continue
                    if (k[1] in [i[1], i[2]]) or (k[2] in [i[1], i[2]]):
                        continue
                    if not isAtRightAngles(k, j):
                        continue
                    
                    for l in edge:
                        if i == l or j == l or k == l:
                            continue
                        if (k[1] not in [l[1], l[2]]) and (k[2] not in [l[1], l[2]]):
                            continue
                        if (i[1] not in [l[1], l[2]]) and (i[2] not in [l[1], l[2]]):
                            continue
                        if not isAtRightAngles(l, k):
                            continue

                        ans = round(calcLength(i) ** 2)
                        break

print(ans)
