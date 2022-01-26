n = int(input())
s = input()
s1 = [""] * n
s2 = [""] * n
for i in range(n):
    s1[i] = s[i]
    s2[i] = s[i + n]
q = int(input())
r = False


def make_ans(s1, s2):
    acc = ""
    for i in s1:
        acc += i
    for i in s2:
        acc += i
    return acc


for i in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        if a <= n and b <= n:
            s1[a - 1], s1[b - 1] = s1[b - 1], s1[a - 1]
        elif a <= n and b > n:
            s1[a - 1], s2[b - n - 1] = s2[b - n - 1], s1[a - 1]
        else:
            s2[a - n - 1], s2[b - n - 1] = s2[b - n - 1], s2[a - n - 1]
    else:
        s1, s2 = s2, s1


ans = make_ans(s1, s2)
print(ans)
