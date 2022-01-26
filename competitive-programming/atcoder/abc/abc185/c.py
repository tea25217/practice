L = int(input())
K = 12

def solver(L, K):
    p = [[0] * 201] * 201
    p[0][0] = 1

    for i in range(1, L + 1):
        for j in range(1, K + 1):
            if (i - j >= 0):
                p[i][j] = (p[i - 1][j - 1] + p[i - j][j]) % 1000000007
            else:
                p[i][j] = p[i - 1][j - 1]

    return p[i][j]

ans = solver(L, K)

print(ans)