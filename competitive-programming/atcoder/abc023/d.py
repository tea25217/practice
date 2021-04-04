# とりあえず写経してみたけど同様の問題を次解ける気がしない
#
# 問題
# https://atcoder.jp/contests/abc023/tasks/abc023_d
# 理解できた解説
# https://scrapbox.io/longshoujin/ABC023_D_-_%E5%B0%84%E6%92%83%E7%8E%8B

n = int(input())
h = [0] * n
s = [0] * n
for i in range(n):
    h[i], s[i] = map(int, input().split())

INF = 2 ** 60
ng, ok = 0, INF


def check(x):
    cnt = [0] * n
    for i in range(n):
        if (x - h[i]) < 0:
            return False
        t = (x - h[i]) // s[i]
        if t < n:
            cnt[t] += 1
    cum = [0] * n
    cum[0] = cnt[0]
    for i in range(0, n - 1):
        cum[i + 1] = cnt[i + 1] + cum[i]
    for t in range(n):
        if cum[t] > t + 1:
            return False
    return True


while (ok - ng > 1):
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)
