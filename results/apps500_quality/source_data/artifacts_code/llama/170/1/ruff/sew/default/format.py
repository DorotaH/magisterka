import sys

n = int(input())
k1 = int(input().split()[0])
k2 = n - k1
deck1 = list(map(int, input().split()))
deck2 = list(map(int, input().split()))

i = 0
while deck1 and deck2:
    if deck1[i] > deck2[i]:
        deck1 += deck2[i], deck1.pop(0)
        deck1 += deck1.pop(1 + i)
    elif deck1[i] < deck2[i]:
        deck2 += deck1[i], deck2.pop(0)
        deck2 += deck2.pop(i + 1)
    else:
        deck1 += deck2[i], deck1.pop(0)
        deck2 += deck1.pop(1 + i)
    i += 1
    if len(deck1) == 0 or len(deck2) == 0:
        break

if deck1:
    print(i + 1, 1)
elif deck2:
    print(i + 1, 2)
else:
    print(-1)
