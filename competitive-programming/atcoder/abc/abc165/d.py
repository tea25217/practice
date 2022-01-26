from math import floor
from decimal import Decimal

a, b, n = map(int, input().split())

ans = floor(Decimal(a * n) / Decimal(b)) - a * floor(Decimal(n) / Decimal(b))

print(ans)