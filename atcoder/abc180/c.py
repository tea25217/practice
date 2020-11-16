n = int(input())
nums = set()

for i in range(1, round(n ** 0.5) + 1):
    if not n % i:
        nums.add(i)
        nums.add(round(n / i))

ans = sorted(list(nums))

for i in ans:
    print(i)