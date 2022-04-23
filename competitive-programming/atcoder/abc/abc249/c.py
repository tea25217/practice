n, k = map(int, input().split())
s = [input() for _ in range(n)]


def cnt(word):
    for c in word:
        letterCnt[ord(c) - 97] += 1


def cnt2(k):
    ans = 0
    for i in letterCnt:
        if i == k:
            ans += 1
    return ans


ans = 0
for i in range(2 ** n):
    letterCnt = [0] * 26
    for j in range(n):
        if (i >> j) & 1:
            cnt(s[j])
    ans = max(ans, cnt2(k))


print(ans)
