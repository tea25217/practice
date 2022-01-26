# RE,TLE

n, q = map(int, input().split())
children = []
kindergarten = [[-1] for i in range(20000)]
highests = [-1] * 20000

for i in range(n):
    a, b = map(int, input().split())
    children.append([a, b])
    kindergarten[b-1].append(a)
    highests[b-1] = max(highests[b-1], a)

for i in range(q):
    c, d  = map(int, input().split())
    former = children[c-1][1]
    rate = children[c-1][0]

    children[c-1][1] = d

    kindergarten[former-1].remove(rate)
    highests[former-1] = max(kindergarten[former-1])

    kindergarten[d-1].append(rate)
    highests[d-1] = max(highests[d-1], rate)

    tmpList  = set(highests)
    tmpList.remove(-1)
    equality = min(tmpList)
    print(equality)