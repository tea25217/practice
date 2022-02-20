a, b = map(int, input().split())

if a + b == 11 or abs(a - b) == 1:
    print("Yes")
else:
    print("No")
