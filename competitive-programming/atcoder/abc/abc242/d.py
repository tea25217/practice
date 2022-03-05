s = input()
q = int(input())


def solver():
    t, k = map(int, input().split())
    count = 0
    while k > 1 and t:
        if k % 2 == 1:
            count += 1
        else:
            count += 2
        k = (k + 1) // 2
        t -= 1

    count += t
    if s[k - 1] == 'A':
        ans = 0
    elif s[k - 1] == 'B':
        ans = 1
    else:
        ans = 2
    ans += count
    ans %= 3

    if ans == 0:
        print('A')
    elif ans == 1:
        print('B')
    else:
        print('C')


for _ in range(q):
    solver()
