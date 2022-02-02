_ = input()
count = {"1": 0, "2": 0, "3": 0}

for i in input().split():
    count[i] += 1


def comb2(n):
    return (n * (n - 1)) // 2


ans = sum(map(comb2, count.values()))

print(ans)
