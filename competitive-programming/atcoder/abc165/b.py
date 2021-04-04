from math import floor
from decimal import Decimal

x = int(input())
amount = 100
count = 0

while amount < x:
    amount += floor(Decimal(amount) / Decimal(100))
    count += 1

print(count)