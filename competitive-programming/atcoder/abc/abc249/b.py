s = input()
words = set()
if s.islower() or s.isupper():
    print('No')
    exit()

for c in s:
    if c in words:
        print('No')
        exit()
    words.add(c)

print('Yes')
