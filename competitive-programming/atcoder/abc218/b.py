p = list(map(int, input().split()))

for i in range(len(p)):
    print(chr(p[i] + 96), end='')
print('')
