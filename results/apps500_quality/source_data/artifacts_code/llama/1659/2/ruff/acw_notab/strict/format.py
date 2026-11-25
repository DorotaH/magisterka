n, x = map(int, input().split())

queue = []
distressed = 0

for _ in range(n):
    c, d = input().split()
    d = int(d)

    if c == "+":
        x += d
    elif x < d:
        distressed += 1
    else:
        x -= d

print(x, distressed)
