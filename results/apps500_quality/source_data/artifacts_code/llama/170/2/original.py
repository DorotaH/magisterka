import sys

def war_game(p1, p2):
    fights = 0
    while len(p1) > 0 and len(p2) > 0:
        fights += 1
        if p1[-1] > p2[-1]:
            p1.extend([p1.pop(), p2.pop()])
        elif p2[-1] > p1[-1]:
            p2.extend([p2.pop(), p1.pop()])
        else:
            if len(p1) >= 3 and len(p2) >= 3:
                p1.extend([p1.pop(), p2.pop()])
                p1.extend([p1.pop(), p2.pop()])
                p2.extend([p2.pop(), p1.pop()])
            elif len(p1) >= 3:
                p1.extend([p1.pop(), p2.pop()])
            else:
                p2.extend([p2.pop(), p1.pop()])
    return fights, p1 or p2

n = int(input())
k1 = int(input().split()[0])
p1 = list(map(int, input().split()))
k2 = int(input().split()[0])
p2 = list(map(int, input().split()))

fights, winner = war_game(p1, p2)
if winner:
    print(fights, 1 if winner == p1 else 2)
else:
    print(-1)
