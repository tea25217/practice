n, x = map(int, input().split())
s = ""
for i in range(26):
    s += chr(65 + i) * n

print(s[x - 1])
