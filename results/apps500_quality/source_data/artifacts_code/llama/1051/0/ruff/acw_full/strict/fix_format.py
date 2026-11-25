k = int(input())
ranks = sorted(map(int, input().split()))

i = 0
declined = 0

while i < k:
    if ranks[i] > i + 1:
        declined += ranks[i] - (i + 1)
    i += 1

print(declined)
