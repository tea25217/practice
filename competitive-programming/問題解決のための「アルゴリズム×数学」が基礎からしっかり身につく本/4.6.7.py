a, b = map(int, input().split())
divider = 1000000007

p = a
ans = 1
for i in range(30):
    if b & (1 << i):
        ans *= p
        ans %= divider
    p *= p
    p %= divider

print(ans)
