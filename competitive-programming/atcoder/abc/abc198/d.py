# 順列全探索の中身を改善しきれずTLE
# https://atcoder.jp/contests/abc198/tasks/abc198_d

from itertools import permutations

s1 = input()
s2 = input()
s3 = input()

letters = set()

for i, c in enumerate(s1 + s2 + s3):
    letters.add(c)

if len(letters) > 10:
    print("UNSOLVABLE")
    exit()

pairs = permutations(list(map(str, range(10))), len(letters))

for pair in pairs:
    if pair[0] == '0':
        continue
    cnt = 0
    n1s = ""
    n2s = ""
    n3s = ""
    d = dict()

    for i in range(len(s1)):
        if s1[i] not in d:
            d[s1[i]] = pair[cnt]
            cnt += 1
        n1s += d[s1[i]]
    for i in range(len(s2)):
        if s2[i] not in d:
            d[s2[i]] = pair[cnt]
            cnt += 1
        n2s += d[s2[i]]
    for i in range(len(s3)):
        if s3[i] not in d:
            d[s3[i]] = pair[cnt]
            cnt += 1
        n3s += d[s3[i]]

    n1 = int(n1s)
    n2 = int(n2s)
    n3 = int(n3s)
    if n1 == 0 or n2 == 0 or n3 == 0:
        continue
    if (len(s1) != len(str(n1))) or (len(s2) != len(str(n2))) or (len(s3) != len(str(n3))):
        continue
    if n1 + n2 == n3:
        break

else:
    print("UNSOLVABLE")
    exit()

for i in (n1, n2, n3):
    print(i)
