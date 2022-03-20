n = int(input())
nums = set(i for i in range(1, 2 * n + 2))

while 1:
    a = nums.pop()
    print(a)

    b = int(input())
    if b == 0:
        exit()
    else:
        nums.remove(b)
