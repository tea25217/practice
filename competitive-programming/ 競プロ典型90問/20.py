from decimal import Decimal


a, b, c = map(int, input().split())

if Decimal(a) < Decimal(c ** b):
    print("Yes")
else:
    print("No")
