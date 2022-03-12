# stackによる解法
from collections import deque


n, x = map(int, input().split())
stack = deque()

for s in input():
    if s == 'U' and stack and stack[-1] != 'U':
        stack.pop()
    else:
        stack.append(s)

while stack:
    s = stack.popleft()

    if s == 'U':
        x //= 2
    elif s == 'L':
        x *= 2
    else:
        x = x * 2 + 1

print(x)
