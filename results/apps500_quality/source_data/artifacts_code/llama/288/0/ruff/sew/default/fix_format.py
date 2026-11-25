n = int(input())
n -= 1  # because we start from 0

games = 0
i = 1
while 1:
    games += 1
    i *= 2
    if i > n:
        break
    i -= 1

print(games)
