# モンテカルロ法(条件満たせず)
import random

REPEAT = 1000000

a, b, c = map(int, input().split())


def solver(a, b, c):

    ans = 0

    while a < 100 and b < 100 and c < 100:
        if a > 0 and b > 0 and c > 0:
            g = random.randrange(3)

            if g == 0:
                a += 1
            elif g == 1:
                b += 1
            else:
                c += 1

        elif a > 0 and b > 0 and c <= 0:
            g = random.randrange(2)

            if g == 0:
                a += 1
            else:
                b += 1

        elif a > 0 and b <= 0 and c > 0:
            g = random.randrange(2)

            if g == 0:
                a += 1
            else:
                c += 1

        elif a <= 0 and b > 0 and c > 0:
            g = random.randrange(2)

            if g == 0:
                b += 1
            else:
                c += 1

        else:
            print(100 - (a + b + c))
            exit()

        ans += 1

    return ans


total = 0

for i in range(REPEAT):
    total += solver(a, b, c)

print(total/REPEAT)
