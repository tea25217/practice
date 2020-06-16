x, y = map(int, input().split())

for i in range(x+1):
    leg = (x-i)*2 + (x-(x-i))*4
    if leg == y:
        print('Yes')
        exit()

print('No')