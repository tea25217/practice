M = 998244353


def modPow(a, b, divider):
    R = 30
    p = a
    ans = 1
    for i in range(R):
        if b & (1 << i):
            ans = (ans * p) % divider
        p = (p ** 2) % divider
    return ans


def solver():
    n = int(input())
    s = input()
    patterns = [ord(c) - ord("A") for c in s]
    mid = (n + 1) // 2
    acc = 0

    for i in range(mid):
        acc = (acc + patterns[i] * modPow(26, (mid - i - 1), M)) % M

    # sの前半の反転がsの後半を辞書順で超えたら-1する
    m = (n + 1) % 2

    for i in range(mid):
        if patterns[mid - i - 1] < patterns[mid + m + i - 1]:
            acc += 1
            break
        if patterns[mid - i - 1] > patterns[mid + m + i - 1]:
            break
    else:
        acc += 1

    acc %= M

    print(acc)


for _ in range(int(input())):
    solver()
