n, q = map(int, input().split())
diff = [0] * n

for i in range(q):
    l, r, x = map(int, input().split())
    diff[l - 1] += x
    if r < n:
        diff[r] -= x

for i in range(n - 1):
    if diff[i + 1] < 0:
        print(">", end="")
    elif diff[i + 1] == 0:
        print("=", end="")
    else:
        print("<", end="")
