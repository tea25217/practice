a, b, c = map(int, input().split())

if not c:
    if a > b:
        print('Takahashi')
    else:
        print('Aoki')
else:
    if a >= b:
        print('Takahashi')
    else:
        print('Aoki')
