_ = input()
a = input().split()
count = {"100": 0, "200": 0, "300": 0, "400": 0}

for i in a:
    count[i] += 1


ans = count["100"] * count["400"] + count["200"] * count["300"]

print(ans)
