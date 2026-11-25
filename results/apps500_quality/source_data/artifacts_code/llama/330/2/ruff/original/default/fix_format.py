import math

p, y = map(int, input().split())

for x in range(p, 0, -1):
    if all(
        y // x > 2
        and (y // x) % 2 == 1
        and not all(
            y // i
            for i in range(2, int(math.sqrt(y // x)) + 1, 2)
            if (y // x) % (y // i) == 0
        )
    ):
        print(y)
        break
else:
    print(-1)
