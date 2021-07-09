# hoge
s = input()
# 1
n = int(input())
# 1 2
a, b = map(int, input().split())
# a0 a1 a2 a3 a4
a = list(map(int, input().split()))
# a00 a01 a02 a03 a04
# a10 a11 a12 a13 a14
# a20 a21 a22 a23 a24
a = [list(map(int, input().split())) for i in range(n)]

# s[n] 初期値:0
backet = [0] * n
# s[n][m] 初期値:0
backet = [[0 for j in range(m)] for i in range(n)]
