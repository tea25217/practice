a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

move_a = v * t
move_b = w * t

dist = abs(b-a) + move_b - move_a

if dist <= 0:
    print("YES")
else:
    print("NO")