import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])

w = list(map(int, data[2:2 + n]))
friends = []

index = 2 + n
for _ in range(m):
    x = int(data[index]) - 1
    y = int(data[1 + index]) - 1
    friends.append((x, y))
    index += 2


def can_survive():
    return not any(w[friend[0]] == 0 and w[friend[1]] == 0 for friend in friends)


if not can_survive():
    print("DEAD")
else:
    print("ALIVE")
    order = []
    for friend in friends:
        if 0 < w[friend[0]]:
            order.append(1 + friend[0])
            w[friend[0]] -= 1
        elif w[friend[1]] > 0:
            order.append(1 + friend[1])
            w[friend[1]] -= 1
    print(' '.join(map(str, order)))
