t = int(input())
n = int(input())
diff = [0] * (t)

for i in range(n):
    L, R = map(int, input().split())
    diff[L] += 1
    if R != t:
        diff[R] -= 1

cusum = [0] * (t)
cusum[0] = diff[0]
print(cusum[0])

for i in range(1, t):
    cusum[i] = cusum[i - 1] + diff[i]
    print(cusum[i])
