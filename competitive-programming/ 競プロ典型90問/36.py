import sys


def main():
    n, q = map(int, sys.stdin.readline().split())
    manhattan = [""] * n

    for i in range(n):
        x, y = map(int, sys.stdin.readline().split())
        manhattan[i] = (x + y, x - y)

    compair = [0] * 4

    for i, j in manhattan:
        compair[0] = max(compair[0], i)
        compair[1] = min(compair[1], i)
        compair[2] = max(compair[2], j)
        compair[3] = min(compair[3], j)

    for _ in range(q):
        qi = int(input())
        d1 = abs(compair[0] - manhattan[qi - 1][0])
        d2 = abs(compair[1] - manhattan[qi - 1][0])
        d3 = abs(compair[2] - manhattan[qi - 1][1])
        d4 = abs(compair[3] - manhattan[qi - 1][1])
        ans = max((d1, d2, d3, d4))
        print(ans)


main()
