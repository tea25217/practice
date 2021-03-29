from copy import deepcopy

k = int(input())
q = set()
board = ["........" for i in range(8)]
command = [list(False for j in range(8)) for i in range(8)]
lr = list(range(8))
lc = list(range(8))


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
    lr.remove(r)
    lc.remove(c)


def dfs(board, command, depth, lr, lc):

    if depth > 7:
        output_board(board)

    new_lr = deepcopy(lr)
    row = new_lr.pop(0)

    for col in lc:
        if command[row][col]:
            continue
        new_lc = deepcopy(lc)
        new_lc.remove(col)
        new_board = deepcopy(board)
        new_command = deepcopy(command)
        new_board[row] = board[row][:col] + "Q" + board[row][col + 1:]
        if depth == 7:
            output_board(new_board)
        add_command(new_command, row, col)
        dfs(new_board, new_command, depth + 1, new_lr, new_lc)


def output_board(board):
    for i in range(8):
        print(board[i])
    exit()


dfs(board, command, k, lr, lc)
