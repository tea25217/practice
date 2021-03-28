n = int(input())
s = input()
used_i = set()
comb = set()

for i in range(n - 2):
    si = s[i]
    if si in used_i:
        continue
    else:
        used_i.add(si)
        used_j = set()
    
    for j in range(i + 1, n - 1):
        sj = s[j]
        if sj in used_j:
            continue
        else:
            used_j.add(sj)
            used_k = set()
    
        for k in range(j + 1, n):
            sk = s[k]
            if sk in used_k:
                continue
            else:
                used_k.add(sk)
                num = si + sj + sk
                comb.add(num)

print(len(comb))
