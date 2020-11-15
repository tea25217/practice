sx, sy, gx, gy = map(int, input().split())

dist_x = gx - sx

shot_x = dist_x * (sy / (sy + gy))

ans = sx + shot_x

print(ans)