n = int(input())
a = list(map(int, input().split()))
ans = 0
sum_current = 0
sum_Ai = 0
dMax_i = 0

for i in range(0, n):
    sum_Ai += a[i]
    dMax_i = max(dMax_i, sum_Ai)
    ans = max(ans, sum_current + dMax_i)
    sum_current += sum_Ai

print(ans)