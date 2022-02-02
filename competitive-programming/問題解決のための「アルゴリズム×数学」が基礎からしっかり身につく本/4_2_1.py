n = int(input())
a = list(map(int, input().split()))
m = int(input())
diff = [0] * (n - 1)
leave = int(input())    # 駅B1

for i in range(1, m):
    arrival = int(input())
    sec_from = min(leave, arrival)
    sec_to = max(leave, arrival)
    diff[sec_from - 1] += 1
    if sec_to != n:
        diff[sec_to - 1] -= 1
    leave = arrival

cusum = [0] * (n - 1)
cusum[0] = diff[0]
ans = cusum[0] * a[0]

for i in range(1, n - 1):
    cusum[i] = cusum[i - 1] + diff[i]
    ans += cusum[i] * a[i]

print(ans)
