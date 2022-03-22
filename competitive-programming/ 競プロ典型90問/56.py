n, s = map(int, input().split())
bags = [tuple(map(int, input().split())) for i in range(n)]
dp = [[False] * (s + 1) for i in range(n + 1)]
dp[0][0] = True

for i in range(1, n + 1):
    a, b = bags[i - 1]
    for j in range(1, s + 1):
        if j < a and j < b:
            continue
        elif j < a:
            dp[i][j] = dp[i - 1][j - b]
        elif j < b:
            dp[i][j] = dp[i - 1][j - a]
        else:
            dp[i][j] = dp[i - 1][j - a] or dp[i - 1][j - b]

if not dp[n][s]:
    print('Impossible')
    exit()

ans = []
j = s
for i in range(n, 0, -1):
    a, b = bags[i - 1]
    if j >= a and dp[i - 1][j - a]:
        ans.append('A')
        j -= a

    else:
        ans.append('B')
        j -= b

for bag in ans[::-1]:
    print(bag, end='')
print()
