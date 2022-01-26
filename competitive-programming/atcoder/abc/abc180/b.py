n = int(input())
tmp_sum = 0
tmp_sq_sum = 0
tmp_max = 0

for i in list(map(int, input().split())):
    abs_x = abs(i)
    tmp_sum += abs_x
    tmp_sq_sum += abs_x ** 2
    tmp_max = max(tmp_max, abs_x)

ans_man = tmp_sum
ans_euc = tmp_sq_sum ** 0.5
ans_che = tmp_max

print(ans_man)
print(ans_euc)
print(ans_che)