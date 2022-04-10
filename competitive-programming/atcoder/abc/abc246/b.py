import math
a, b = map(int, input().split())
t = math.atan2(b, a)
x = math.cos(t)
y = math.sin(t)
print(x, y)
