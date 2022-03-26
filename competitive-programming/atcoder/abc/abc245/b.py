n = int(input())
a = list(map(int, input().split()))

bucket = [False] * (2000 + 2)

for i in a:
    bucket[i] = True

for i in range(2002):
    if not bucket[i]:
        print(i)
        exit()
