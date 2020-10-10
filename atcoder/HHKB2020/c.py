n = int(input())
p = list(range(200001))
currentMin = 0
for i in map(int, input().split()):
    if p[i] == 200001:
        print(currentMin)
        continue
    p[i] = 200001
#    for j in p[currentMin + 1:]:
#        if j != 200001:
#            currentMin = j
#            break
#    currentMin2 = min(p[currentMin + 1:])
#    currentMin = min(currentMin, currentMin2)
    currentMin = min(p)
    print(currentMin)