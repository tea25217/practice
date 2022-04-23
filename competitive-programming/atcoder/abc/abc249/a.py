a, b, c, d, e, f, x = map(int, input().split())


takahashi = aoki = 0
cnt_takahashi = cnt_aoki = 0
cnt2_takahashi = cnt2_aoki = 0

for i in range(x):
    if cnt_takahashi < a:
        takahashi += b
        cnt_takahashi += 1
    else:
        cnt2_takahashi += 1
        if cnt2_takahashi == c:
            cnt_takahashi = cnt2_takahashi = 0
    if cnt_aoki < d:
        aoki += e
        cnt_aoki += 1
    else:
        cnt2_aoki += 1
        if cnt2_aoki == f:
            cnt_aoki = cnt2_aoki = 0

if takahashi > aoki:
    print("Takahashi")
elif aoki > takahashi:
    print("Aoki")
else:
    print("Draw")
