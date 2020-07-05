n = int(input())
ans = [0] * 4

for i in range(n):
    judge = input()
    if judge == "AC":
        ans[0] += 1
    elif judge == "WA":
        ans[1] += 1
    elif judge == "TLE":
        ans[2] += 1
    else:
        ans[3] += 1

print("AC x " + str(ans[0]))
print("WA x " + str(ans[1]))
print("TLE x " + str(ans[2]))
print("RE x " + str(ans[3]))