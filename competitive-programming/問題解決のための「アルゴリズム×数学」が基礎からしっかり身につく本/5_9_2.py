n = int(input())
a = list(sorted(list(map(int, input().split()))))
b = list(sorted(list(map(int, input().split()))))

ans = sum(map(lambda x, y: abs(x - y), a, b))
print(ans)
