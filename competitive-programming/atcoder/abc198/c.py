# https://atcoder.jp/contests/abc198/tasks/abc198_c

r, x, y = map(int, input().split())

dist = (x ** 2 + y ** 2) ** 0.5

if dist // r < 1:
    print(2)
    exit()

ans = dist // r if dist % r == 0 else (dist // r) + 1

print(int(ans))
