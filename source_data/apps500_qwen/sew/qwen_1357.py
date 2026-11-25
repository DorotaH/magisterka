import sys
input = sys.stdin.read
data = input().split()

n, m = int(data[0]), int(data[1])

w, friends = list(map(int, data[2:2+n])), []

index = n + 2
for  i in  range(m):
    x, y = int(data[index]) - 1, int(data[index + 1]) - 1
    friends.append((x, y))
    index = index + 2


def can_survive():
    for friend in friends:
        if w[friend[0]] == 0 and w[friend[1]] == 0:
            return  False
    return True

if not can_survive():
    print("DEAD")
else:
    print("ALIVE")
    order = []
    for friend in friends:
        if w[friend[0]] > 0:
            order.append(friend[0] + 1)
            w[friend[0]] -= 1
        elif w[friend[1]] > 0:
            order.append(friend[1] + 1)
            w[friend[1]] -= 1
    print(' '.join(map(str, order)))
