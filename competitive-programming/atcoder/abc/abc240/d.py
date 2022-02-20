from collections import deque

n = int(input())
a = list(map(int, input().split()))

pipe = deque([])

for i in range(n):
    if len(pipe) == 0:
        pipe.append((a[i], 1))
    else:
        lastN = pipe[-1][0]
        if a[i] == lastN:
            lastC = pipe[-1][1]
            if a[i] == lastC + 1:
                for j in range(lastC):
                    _ = pipe.pop()
            else:
                pipe.append((a[i], lastC + 1))
        else:
            pipe.append((a[i], 1))
    print(len(pipe))
