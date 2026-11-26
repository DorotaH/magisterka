n, x = map(int, input().split())

queue = []
distressed = 0

for _ in range(n):
    c, d = input().split()
    d = int(d)

    if not c == "+":
        if x < d:
            distressed += 1
        else:
            x -= d
    else:
        x += d

print(x, distressed)
