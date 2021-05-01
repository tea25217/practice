n, d_ufo, h_ufo = map(int, input().split())
d = [0] * n
h = [0] * n
for i in range(n):
    d[i], h[i] = map(int, input().split())


def calcDegree(d, h):
    return h / d


a_min = 1000
a_min_i = -1
for i in range(n):
    a_current = calcDegree(d_ufo - d[i], h_ufo - h[i])
    if a_current < a_min:
        a_min = a_current
        a_min_i = i


a_tower_to_i = calcDegree(d[a_min_i], h[a_min_i])
a_tower_to_ufo = calcDegree(d_ufo, h_ufo)

if a_tower_to_ufo >= a_tower_to_i:
    print(0)
else:
    ans = h[a_min_i] - a_min * d[a_min_i]
    print(ans)
