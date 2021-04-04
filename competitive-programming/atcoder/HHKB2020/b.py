h, w = map(int, input().split())
masu = [0] * h
for i in range(h):
    masu[i] = input()
ans = 0

for i in range(h):
    for j in range(w):
        if (masu[i][j] != '.'):
            continue
        else:
            if (i == h - 1) and (j == w - 1):
                break
            elif (i == h - 1):
                if (masu[i][j + 1] == '.'):
                    ans += 1
            elif (j == w - 1):
                if (masu[i + 1][j] == '.'):
                    ans += 1
            else:
                if (masu[i][j + 1] == '.'):
                    ans += 1
                if (masu[i + 1][j] == '.'):
                    ans += 1

print(ans)