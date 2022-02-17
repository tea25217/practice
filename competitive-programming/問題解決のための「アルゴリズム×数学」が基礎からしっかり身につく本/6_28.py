n = int(input())
c = input()


def getNewColor(s):
    """部分ピラミッド頂上のブロックを決定する
        Args:
            s[str]: 部分ピラミッド
        Returns:
            [str]: 部分ピラミッド頂上のブロックが何色か
    """
    L = s[0]
    R = s[-1]
    if L == R:
        return L
    return list({'B', 'W', 'R'} - {L, R})[0]


def getNewStep(s, n):
    """n段上のブロックを決定する
        Args:
            s[str]: 元の段
            n[int]: 何段上のブロックを生成するか
        Returns:
            [str]: n段上のブロック
        Note:
            前提条件: n > 0, nは3の累乗
    """
    return ''.join(list(getNewColor(s[i:i + n + 1]) for i in range(len(s) - n)))


for k in range(12, -1, -1):
    d = 3 ** k
    if n < d + 1:
        continue
    while n >= d + 1:
        n -= d
        c = getNewStep(c, d)

print(c)
