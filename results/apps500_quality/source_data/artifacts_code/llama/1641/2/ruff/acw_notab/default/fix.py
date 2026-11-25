
n, k, s, t = map(int, input().split())
c = []
v = []
for _ in range(n):
    c.append(int(input().split()[0]))
    v.append(int(input().split()[1]))

g = list(map(int, input().split()))


def possible(car):
    tank = car[1]
    time = 0
    for i in range(k):
        dist = g[i] - (i == 0 and 0 or g[i - 1])
        time += min(2 * dist, 2 * tank)
        if t < time:
            return False
        if 2 * dist > 2 * tank:
            tank -= dist
            if 0 >= tank:
                return False
    return True


c.sort()
v.sort()
for i in range(n):
    if possible([c[i], v[i]]):
        print(c[i])
        break
else:
    print(-1)
