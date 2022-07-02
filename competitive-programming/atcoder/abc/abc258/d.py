n, x = map(int, input().split())
stages = [[0] * 2 for i in range(n)]
for i in range(n):
    stages[i][0], stages[i][1] = map(int, input().split())

stageToReplay = [-1] * n
minB = float("inf")
minStage = 0

for i in range(n):
    if stages[i][1] < minB:
        minB = stages[i][1]
        minStage = i
    stageToReplay[i] = minStage

ans = [float("inf")] * n
t = 0

for i in range(n):
    t += stages[i][0] + stages[i][1]
    x -= 1
    ans[i] = t + x * stages[stageToReplay[i]][1]
    if x == 0:
        break

print(min(ans))
