# 順列全探索での解法

from copy import deepcopy
from itertools import permutations

k = int(input())
q = set()
board = ["........" for i in range(8)]
command = [list(False for j in range(8)) for i in range(8)]
lc = []


def add_command(command, r, c):
    for col in range(8):
        command[r][col] = True
    for row in range(8):
        command[row][c] = True
    # 左上へ向かう
    dr, dc = -1, -1
    while (r + dr >= 0) and (c + dc >= 0):
        command[r + dr][c + dc] = True
        dr += -1
        dc += -1
    # 右下へ向かう
    dr, dc = 1, 1
    while (r + dr < 8) and (c + dc < 8):
        command[r + dr][c + dc] = True
        dr += 1
        dc += 1
    # 右上へ向かう
    dr, dc = -1, 1
    while (r + dr >= 0) and (c + dc < 8):
        command[r + dr][c + dc] = True
        dr += -1
        dc += 1
    # 左下へ向かう
    dr, dc = 1, -1
    while (r + dr < 8) and (c + dc >= 0):
        command[r + dr][c + dc] = True
        dr += 1
        dc += -1


for i in range(k):
    r, c = map(int, input().split())
    board[r] = board[r][:c] + "Q" + board[r][c + 1:]
    add_command(command, r, c)
    lc.append(c)


patterns = permutations(range(8))


def check_pattern(pattern, lc, base_board, base_command):
    board = deepcopy(base_board)
    command = deepcopy(base_command)
    for row, col in enumerate(pattern):
        if col in lc:
            continue
        if command[row][col]:
            return (False, board)
        board[row] = board[row][:col] + "Q" + board[row][col + 1:]
        add_command(command, row, col)
    return (True, board)


def output_board(board):
    for i in range(8):
        print(board[i])
    exit()


for pattern in patterns:
    isOK, result = check_pattern(pattern, lc, board, command)
    if isOK:
        output_board(result)
