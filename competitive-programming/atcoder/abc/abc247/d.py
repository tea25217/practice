from collections import deque


n = int(input())
q = [input() for _ in range(n)]
q1 = deque([])
q2 = deque([])

for i in q:
    if i[0] == '1':
        _, x, c = map(int, i.split())
        q1.append([x, c])
    else:
        _, c = map(int, i.split())
        q2.append(c)

while q2:
    b = 0
    need = q2.popleft()
    num = 0
    while need:
        if q1[0][1] <= need:
            b += q1[0][1]
            need -= q1[0][1]
            num += q1[0][0] * q1[0][1]
            q1.popleft()
        else:
            b += need
            num += q1[0][0] * need
            q1[0][1] -= need
            need = 0
    print(num)
