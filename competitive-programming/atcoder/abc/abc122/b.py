S = input()

start = 0
end = 0
ans = 0

for i in range(len(S)):
    current = i
    if S[current] in ['A', 'C', 'G', 'T']:
        ans = max(ans, end - start + 1)
        end += 1
    else:
        start = i + 1
        end = i + 1

print(ans)
