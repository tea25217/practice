_ = input()
a = map(int, input().split())
b = map(int, input().split())

ans = sum(a) / 3 + sum(b) * 2 / 3

print(ans)
