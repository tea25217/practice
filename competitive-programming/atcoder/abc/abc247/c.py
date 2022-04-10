n = int(input())


def makeN(n):
    if n == 1:
        print(n, end="")
    else:
        makeN(n - 1)
        print(" " + str(n), end=" ")
        makeN(n - 1)


makeN(n)
