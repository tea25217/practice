ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

# ベクトルの成分表示
BA = (ax - bx, ay - by)
BC = (cx - bx, cy - by)
CA = (ax - cx, ay - cy)
CB = (bx - cx, by - cy)


# 鈍角か判定
def isAngleObtuse(a, b):
    innerProduct = a[0] * b[0] + a[1] * b[1]
    if innerProduct < 0:
        return True
    else:
        return False


isAngleABCObtuse = isAngleObtuse(BA, BC)
isAngleACBObtuse = isAngleObtuse(CA, CB)

# 角ABCか角ACBが鈍角の場合、点Aと線分BCの端との距離 => BAないしCAの長さが答え
if isAngleABCObtuse:
    ans = (BA[0] ** 2 + BA[1] ** 2) ** 0.5
elif isAngleACBObtuse:
    ans = (CA[0] ** 2 + CA[1] ** 2) ** 0.5
# それ以外の場合、平行四辺形の面積(BA,BCの外積)を底辺(線分BC)で割って高さ(AからBCへの垂線)を求める
else:
    S = abs(BA[0] * BC[1] - BA[1] * BC[0])
    distBC = (BC[0] ** 2 + BC[1] ** 2) ** 0.5
    ans = S / distBC

print(ans)
