from itertools import combinations

while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        exit()
    if n < 2 or x < 6:
        print(0)
        continue

    patterns = combinations(range(1, n + 1), 3)
    ans = 0
    for i in patterns:
        if sum(i) == x:
            ans += 1

    print(ans)
