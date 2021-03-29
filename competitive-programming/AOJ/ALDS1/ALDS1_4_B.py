def binary_search(s, t):
    l = 0
    r = len(s)
    while l < r:
        mid = (l + r) // 2
        if s[mid] == t:
            return True
        if s[mid] > t:
            r = mid
        else:
            l = mid + 1
    return False


n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))

acc = 0

for i in t:
    if binary_search(s, i):
        acc += 1

print(acc)
