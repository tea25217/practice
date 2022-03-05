N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))


def whetherAisCutUpAtLeastX(x):
    cut = 0
    size = 0
    for i in range(N + 1):
        if i == 0:
            size += A[0]
        elif i == N:
            size += L - A[i - 1]
        else:
            size += A[i] - A[i - 1]
        if size >= x:
            cut += 1
            size = 0

        # 長さxで分割できた際に、残りの長さがx以上か
        if cut == K:
            if i < N:
                remain = L - A[i]
            else:
                remain = 0
            if remain < x:
                return False
            else:
                return True

    # 長さxで分割できなかった場合
    return False


l = -1
r = L + 1

while r - l > 1:
    x = l + (r - l) // 2
    if whetherAisCutUpAtLeastX(x):
        l = x
    else:
        r = x

print(l)
