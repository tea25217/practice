n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in a:
    if i <= 10:
        continue
    else:
        ans += i - 10
print(ans)
