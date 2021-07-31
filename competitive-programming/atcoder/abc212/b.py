s = input()

if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
    print('Weak')
    exit()

for i in range(1, len(s)):
    if s[i - 1] == '9':
        if s[i] == '0':
            continue
        else:
            break
    else:
        if int(s[i - 1]) + 1 == int(s[i]):
            continue
        else:
            break
else:
    print('Weak')
    exit()

print('Strong')
