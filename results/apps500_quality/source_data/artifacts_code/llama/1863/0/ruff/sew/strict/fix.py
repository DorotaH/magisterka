import sys

n, eggs = int(input()), []
for  _ in  range(n):
    a, g = map(int, input().split())
    eggs.append((a, g))

# Sort the eggs by the difference between a and g in descending order
eggs.sort(key=lambda  x: (x[0] - x[1], x[1]))

ans = ""
sa, sg = 0, 0
for  i in  range(n):
    if not i % 2 == 0:
        ans += 'A'
        sa += eggs[i][1]
    else:
        ans += 'G'
        sa += eggs[i][0]
    sg += eggs[i][1]

    if sg - sa > 500:
        print(-1)
        sys.exit()

if not abs(sg - sa) <= 500:
    print(-1)
else:
    print(ans)
