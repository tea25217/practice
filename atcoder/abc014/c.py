n = int(input())
BRIGHTNESS_MAX = 1000002

table = [0] * BRIGHTNESS_MAX

for i in range(n):
    a, b = map(int, input().split())
    table[a] += 1
    table[b + 1] -= 1

cusum = 0
votes_of_most_popular = 0
most_popular = 0

for i in range(BRIGHTNESS_MAX):
    cusum += table[i]
    if cusum > votes_of_most_popular:
        votes_of_most_popular = cusum

print(votes_of_most_popular)