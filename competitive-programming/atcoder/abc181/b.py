n = int(input())
cumulativeSum = [0] * 1000001

for i in range(1,1000001):
    cumulativeSum[i] = cumulativeSum[i - 1] + i

ans = 0

for i in range(n):
    a, b = map(int, input().split())
    ans += cumulativeSum[b] - cumulativeSum[a - 1]

print(ans)