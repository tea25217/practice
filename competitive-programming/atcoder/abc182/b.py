n = int(input())
nums = list(map(int, input().split()))
ans = 0
gcd = 0

for i in range(2, 1001):
    current_gcd = 0
    for j in nums:
        if j % i == 0:
            current_gcd += 1
    if current_gcd > gcd:
        ans = i
        gcd = current_gcd

print(ans)