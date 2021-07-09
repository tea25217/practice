# 半端なまま放置しているが一旦push
# 総当りの凄まじく遅いNonogramソルバー

from dataclasses import dataclass
from copy import deepcopy


@dataclass
class Board:
    rowNums: list[list[int]]
    colNums: list[list[int]]
    row: int
    col: int


class Solver:
    def __init__(self, board: Board):
        self.row = board.row
        self.col = board.col
        self.reset()
        self.rowNums = deepcopy(board.rowNums)
        self.colNums = deepcopy(board.colNums)

    def reset(self):
        self.answer = [[False for j in range(self.col)] for i in range(self.row)]

    def checkAnswerRowNum(self):
        for i in range(self.row):
            currentCol = 0
            currentNums = deepcopy(self.rowNums[i])
            if not currentNums:
                continue

            while currentNums:
                num = currentNums.pop()
                if num == 0:
                    continue
                if currentCol + num > self.col:
                    return False

                while currentCol < self.col:
                    if self.answer[i][currentCol] is False:
                        currentCol += 1
                    else:
                        break
                else:
                    return False

                for i in range(num):
                    if self.answer[i][currentCol] is False:
                        return False
                    currentCol += 1
        return True


    def checkAnswerColNum(self):
        for i in range(self.col):
            currentRow = 0
            currentNums = deepcopy(self.colNums[i])
            if not currentNums:
                continue

            while currentNums:
                num = currentNums.pop()
                if num == 0:
                    continue
                if currentRow + num > self.row:
                    return False

                while currentRow < self.row:
                    if self.answer[currentRow][i] is False:
                        currentRow += 1
                    else:
                        break
                else:
                    return False

                for i in range(num):
                    if self.answer[currentRow][i] is False:
                        return False
                currentRow += 1
        return True


    def checkAnswer(self):
        return self.checkAnswerRowNum() and self.checkAnswerColNum()


    def solve(self):
        rowcol = self.row * self.col
        for i in range(2 ** rowcol):
            self.reset()
            for j in range(rowcol):
                if ((i >> j) & 1):
                    targetRow = j // self.col
                    targetCol = j % self.col
                    self.answer[targetRow][targetCol] = True

            if self.checkAnswer():
                return self.answer

        return None


class CLI:
    def __init__(self):
        pass


    def readBoardInfo(self):
        print('盤面サイズをカンマ区切りの縦,横で入力してください（例:"5,5"）')
        self.row, self.col = map(int, input().split(','))
        self.rowNums = []
        self.colNums = []
        for i in range(1, self.col + 1):
            print('縦のヒント、左から{0}列目をカンマ区切りで入力してください（空の場合は0を入力）'.format(i))
            self.rowNums.append(list(map(int, input().split(','))))
        for i in range(1, self.row + 1):
            print('横のヒント、上から{0}列目をカンマ区切りで入力してください（空の場合は0を入力）'.format(i))
            self.colNums.append(list(map(int, input().split(','))))

        self.board = Board(self.rowNums, self.colNums, self.row, self.col)


    def printAnswer(self, answer):
        for i in range(self.row):
            for j in range(self.col):
                if answer[i][j]:
                    print('0', end='')
                else:
                    print('X', end='')
            print()


    def solveBoard(self):
        solver = Solver(self.board)
        print('探索を開始します')
        answer = solver.solve()
        if answer is None:
            print('条件に合致する解答が見つかりませんでした')
        else:
            self.printAnswer(answer)


def main():
    cli = CLI()
    cli.readBoardInfo()
    cli.solveBoard()


if __name__ == "__main__":
    main()
