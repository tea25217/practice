n = int(input())

def solver(n):
    if n<=26:
        return chr(96+n)
    elif n%26==0:
        return solver(n//26-1)+chr(122)
    else:
        return solver(n//26)+chr(96+n%26)

print(solver(n))