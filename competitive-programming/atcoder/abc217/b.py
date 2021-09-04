contests = {"ABC", "ARC", "AGC", "AHC"}

for c in range(3):
    contests.remove(input())

print(list(contests)[0])
