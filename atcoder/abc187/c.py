n = int(input())
s = set()

for i in range(n):
    s.add(input())

for i in s:
    t = '!' + i
    if t in s:
        print(i)
        exit()
else:
    print('satisfiable')
