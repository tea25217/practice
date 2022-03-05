n = int(input())


def check(s):
    open = 0
    close = 0
    for i in s:
        if i == "(":
            open += 1
        else:
            close += 1
        if close > open:
            return False
    if open == close:
        return True
    else:
        return False


for i in range(2 ** n):
    ans = ""
    for j in range(n):
        if i & (1 << j):
            ans = ")" + ans
        else:
            ans = "(" + ans
    if check(ans):
        print(ans)
