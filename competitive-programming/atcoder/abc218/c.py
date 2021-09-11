# バグが取れなくてお通夜になった跡地

import itertools

n = int(input())
grid1 = [input() for i in range(n)]
grid2 = [input() for i in range(n)]

# Sの始点終点を走査
s_top = 999
s_bottom = -1
s_left = 999
s_right = -1

for i in range(n):
    for j in range(n):
        if grid1[i][j] == '#':
            s_top = min(s_top, i)
            s_bottom = max(s_bottom, i)
            s_left = min(s_left, j)
            s_right = max(s_right, j)

s_height = s_bottom - s_top + 1
s_width = s_right - s_left + 1

# Tの始点終点を走査
t_top = 999
t_bottom = -1
t_left = 999
t_right = -1

for i in range(n):
    for j in range(n):
        if grid2[i][j] == '#':
            t_top = min(t_top, i)
            t_bottom = max(t_bottom, i)
            t_left = min(t_left, j)
            t_right = max(t_right, j)

# 4点から一致を確認していく
# 1.同一角度
if (t_top + s_height) >= n or (t_left + s_width) >= n:
    pass
else:
    for i, j in itertools.product(range(s_height), range(s_width)):
        if grid1[s_top + i][s_left + j] != grid2[t_top + i][t_left + j]:
            break
    else:
        print('Yes')
        exit()

# 2.右に90度回転
if (t_top + s_width) >= n or (t_right - s_height) < 0:
    pass
else:
    for i, j in itertools.product(range(s_height), range(s_width)):
        if grid1[s_top + i][s_left + j] != grid2[t_top + j][t_right - i]:
            break
    else:
        print('Yes')
        exit()

# 3.180度回転
if (t_bottom - s_height) < 0 or (t_right - s_width) < 0:
    pass
else:
    for i, j in itertools.product(range(s_height), range(s_width)):
        if grid1[s_top + i][s_left + j] != grid2[t_bottom - i][t_right - j]:
            break
    else:
        print('Yes')
        exit()

# 4.270度回転
if (t_left + s_height) >= n or (t_bottom - s_width) < 0:
    pass
else:
    for i, j in itertools.product(range(s_height), range(s_width)):
        if grid1[s_top + i][s_left + j] != grid2[t_bottom - j][t_left + i]:
            break
    else:
        print('Yes')
        exit()

print('No')
