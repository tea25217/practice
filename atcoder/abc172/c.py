from collections import deque

n, m, k = map(int, input().split())
*a, = map(int, input().split())
*b, = map(int, input().split())

a = deque(a)
b = deque(b)

t = 0
cnt = 0

while t < k:
    if a and b:
        if a[0] <= b[0]:
            t += a.popleft()
        else:
            t += b.popleft()
        cnt += 1
    elif a:
        t += a.popleft()
        cnt += 1
    elif b:
        t += b.popleft()
        cnt += 1
    else:
        break

if t > k:
    cnt -= 1

print(cnt)