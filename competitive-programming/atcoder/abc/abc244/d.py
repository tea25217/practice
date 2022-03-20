s1, s2, s3 = input().split()
t1, t2, t3 = input().split()

if s1 == t1:
    if s2 == t2:
        print('Yes')
    else:
        print('No')
elif s1 == t3:
    if s2 == t1:
        print('Yes')
    else:
        print('No')
else:
    if s3 == t1:
        print('Yes')
    else:
        print('No')
