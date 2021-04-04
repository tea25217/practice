# 1つの街で演説するごとに票差が2A+B変化する
# 2A+Bが大きい街から順に演説

n = int(input())
towns = []
diff = 0
ans = 0

for i in range(n):
    a, b = map(int, input().split())
    towns.append(2 * a + b)
    diff -= a

towns.sort()

while diff <= 0:
    diff += towns.pop()
    ans += 1

print(ans)
