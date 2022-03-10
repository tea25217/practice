n, k = map(int, input().split())
a = list(map(int, input().split()))

elm = dict()
length = 0
ans = 0
L = 1
R = 0

while L < n and R < n:
    # k種類以下かつ右がはみ出さないなら伸ばす
    if len(elm) <= k and R < n:
        R += 1
        length += 1
        e = a[R - 1]

        if e not in elm:
            elm[e] = 1
        else:
            elm[e] += 1

    if len(elm) <= k:
        ans = max(length, ans)

    # k種類を超えたら、右を追い越さない範囲で縮める
    if len(elm) > k and L < R or R == n:
        e = a[L - 1]
        L += 1
        length -= 1

        elm[e] -= 1
        if elm[e] == 0:
            del elm[e]

print(ans)
