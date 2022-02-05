acc = 0
count = 0
while 1:
    count += 1
    acc += 1 / count
    if count % 10000000 == 0:
        print(f"N: {count} acc: {acc}")
    if acc >= 30:
        print(f"N: {count} acc: {acc}")
        break
