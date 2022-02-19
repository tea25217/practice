from decimal import *
x = Decimal(input())
if x < 0 and x % Decimal(10) != 0:
    f = True
else:
    f = False
x //= Decimal(10)
if f:
    x -= 1
print(x)
