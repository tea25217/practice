n = int(input())
sections = [tuple(map(int, input().split())) for i in range(n)]
diff = [0] * (2 * 10 ** 5 + 1)
cusum = 0
ans = []

for i in range(n):
    L, R = sections[i]
    diff[L] += 1
    diff[R] -= 1

left = 99999999

for i in range(1, (2 * 10 ** 5 + 1)):
    if diff[i] == 0:
        continue
    left = min(left, i)
    cusum += diff[i]
    if cusum == 0:
        ans.append((left, i))
        left = 99999999

for i in ans:
    print(*i)
