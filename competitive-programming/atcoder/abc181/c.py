n = int(input())
dots = [[0] * 2 for i in range(n)]

for i in range(n):
    x, y = map(int, input().split())
    dots[i][0] = x
    dots[i][1] = y

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            #タテ
            if (dots[i][0] == dots[j][0]) and (dots[i][0] == dots[k][0]):
                print("Yes")
                exit()
            #ヨコ
            if (dots[i][1] == dots[j][1]) and (dots[i][1] == dots[k][1]):
                print("Yes")
                exit()
            #ナナメ
            if (dots[i][0] == dots[j][0]) or (dots[i][0] == dots[k][0]) or (dots[j][0] == dots[k][0]):
                continue
            if (dots[j][1] - dots[i][1]) / (dots[j][0] - dots[i][0]) == (dots[k][1] - dots[i][1]) / (dots[k][0] - dots[i][0]):
                print("Yes")
                exit()

print("No")