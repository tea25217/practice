n = int(input())
towns = []
aoki = 0
takahashi = 0
ans = 0

for i in range(n):
    a, b = map(int, input().split())
    towns.append([a, b])
    aoki += a

towns.sort(key=sum, reverse=True)

while takahashi <= aoki:
    t = towns.pop(0)
    aoki -= t[0]
    takahashi += (t[0] + t[1])
    ans += 1

print(ans)
