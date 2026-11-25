k = int(input())
ranks = sorted(map(int, input().split()))

i = declined = 0

while i < k:
    if ranks[i] > i + 1:
        declined += ranks[i] - (1 + i)
    i += 1

print(declined)
