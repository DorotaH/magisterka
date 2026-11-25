def card_war():
    n = int(input())
    k1 = int(input().split()[0])
    k2 = n - k1
    p1 = list(map(int, input().split()))
    p2 = list(map(int, input().split()))

    fights = 0
    while p1 and p2:
        fights += 1
        if p2[-1] < p1[-1]:
            p1.extend([p1.pop(), p2.pop()])
        elif p2[-1] > p1[-1]:
            p2.extend([p1.pop(), p2.pop()])
        else:
            # Swap the cards and continue the game
            p1, p2 = p2, p1
            fights += 1

    if p1:
        print(fights, 1)
    else:
        print(fights, 2)


card_war()
