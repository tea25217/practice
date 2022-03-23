h, w = map(int, input().split())
p = [list(map(int, input().split())) for i in range(h)]
ans = 0

for i in range(1, 2 ** h):
    numMap = dict()
    for j in range(w):
        num = -1
        for k in range(h):
            if (i >> k) & 1:
                if num == -1:
                    num = p[k][j]
                else:
                    if num != p[k][j]:
                        break
        else:
            if num in numMap:
                numMap[num] += 1
            else:
                numMap[num] = 1
    if not numMap:
        continue
    y = max(numMap.values())
    x = bin(i).count('1')
    ans = max(ans, x * y)

print(ans)
