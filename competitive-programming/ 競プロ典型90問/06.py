n, k = map(int, input().split())
s = input()

last = [-1] * 26
nextLetterIndexes = [[-1 for j in range(26)] for i in range(n)]

for i, c in enumerate(s[::-1]):
    letterNum = ord(c) - 97
    idx = n - i - 1
    last[letterNum] = idx
    for i in range(26):
        nextLetterIndexes[idx][i] = last[i]

ans = ""
idx = 0

for i in range(k):
    for j in range(26):
        nextIdx = nextLetterIndexes[idx][j]
        if nextIdx < 0:
            continue
        if n - nextIdx + 1 >= k - i + 1:
            ans += s[nextIdx]
            idx = nextIdx + 1
            break

print(ans)
