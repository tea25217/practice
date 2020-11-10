import copy

nums = [int(x) for x in list(input())]
ans = 99

def checkMultipleOf3(nums):
    if sum(nums) % 3 == 0:
        return True
    else:
        return False

for i in range(2 ** len(nums) -1):
    tmp_n = nums.copy()
    cnt = 0
    for j in range(len(nums)):
        if ((i >> j) & 1):
            tmp_n[len(nums) -1 -j] = 0
            cnt += 1
    if checkMultipleOf3(tmp_n):
        ans = min(ans, cnt)

if ans == 99:
    print(-1)
else:
    print(ans)