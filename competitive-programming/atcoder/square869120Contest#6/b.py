n = int(input())
customer = [list(map(int, input().split())) for i in range(n)]
entrance = []
outlet = []
for i in range(n):
    entrance.append(customer[i][0])
    outlet.append(customer[i][1])

ans = 10 ** 11

for i in entrance:
    for j in outlet:
        acc = 0
        for k in range(n):
            human = customer[k]
            a = abs(human[0] - i)
            b = abs(human[1] - human[0])
            c = abs(j - human[1])
            acc += a + b + c
        ans = min(ans, acc)

print(ans)
