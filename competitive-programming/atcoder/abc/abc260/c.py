n, x, y = map(int, input().split())

red = [0] * (n + 1)
blue = [0] * (n + 1)

red[n] = 1


def changeRed(n):
    i = red[n]
    red[n] = 0
    red[n - 1] += i
    blue[n] += i * x


def changeBlue(n):
    i = blue[n]
    blue[n] = 0
    red[n - 1] += i
    blue[n - 1] += i * y


for i in range(n, 1, -1):
    changeRed(i)
    changeBlue(i)

print(blue[1])
