import math

n = math.floor(int(input()) * 1.08)
p = 206

if n < p:
    print('Yay!')
elif n == p:
    print('so-so')
else:
    print(':(')
