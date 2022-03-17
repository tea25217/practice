# 01-BFSでどうにも削りきれないため、突き当たるまで進むBFSでやる
from collections import deque
import sys


def main():
    h, w = map(int, sys.stdin.readline().split())
    rs, cs = map(int, sys.stdin.readline().split())
    rt, ct = map(int, sys.stdin.readline().split())
    grid = [sys.stdin.readline() for i in range(h)]
    rs -= 1
    cs -= 1
    rt -= 1
    ct -= 1
    q = deque([(rs, cs, 0, 0), (rs, cs, 0, 1)])     # 縦、横、回数、縦or横
    seen0 = [[False for j in range(w)] for i in range(h)]
    seen1 = [[False for j in range(w)] for i in range(h)]
    seen0[rs][cs] = True
    seen1[rs][cs] = True

    def checkExit(row, col):
        if (row, col) == (rt, ct):
            print(t)
            exit()

    while q:
        row, col, t, d = q.popleft()
        if d == 0:
            newRow = row + 1
            while newRow < h and grid[newRow][col] == '.' and not seen0[newRow][col]:
                checkExit(newRow, col)
                seen0[newRow][col] = True
                q.append((newRow, col, t + 1, 1))
                newRow += 1

            newRow = row - 1
            while newRow >= 0 and grid[newRow][col] == '.' and not seen0[newRow][col]:
                checkExit(newRow, col)
                seen0[newRow][col] = True
                q.append((newRow, col, t + 1, 1))
                newRow -= 1

        else:
            newCol = col + 1
            while newCol < w and grid[row][newCol] == '.' and not seen1[row][newCol]:
                checkExit(row, newCol)
                seen1[row][newCol] = True
                q.append((row, newCol, t + 1, 0))
                newCol += 1

            newCol = col - 1
            while newCol >= 0 and grid[row][newCol] == '.' and not seen1[row][newCol]:
                checkExit(row, newCol)
                seen1[row][newCol] = True
                q.append((row, newCol, t + 1, 0))
                newCol -= 1


if __name__ == "__main__":
    main()
