s = input()


def isDifficult(s):
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i].isupper():
                return False
        else:
            if s[i].islower():
                return False
    return True


def solver(s):
    if isDifficult(s):
        print("Yes")
    else:
        print("No")


solver(s)
