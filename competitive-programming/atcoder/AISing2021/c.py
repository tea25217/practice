n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

backet = [0] * (10 ** 5 + 1)

for i in c:
    backet[b[i - 1]] += 1

ans = 0

for i in a:
    ans += backet[i]

print(ans)
