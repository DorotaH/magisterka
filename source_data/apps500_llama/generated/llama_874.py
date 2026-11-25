import sys

a, b, c, d = map(int, sys.stdin.readline().split())

turn = 0
while True:
    turn = (turn + 1) % 2
    if turn == 0:
        c -= b
    else:
        a -= d
    if a <= 0 or c <= 0:
        print('Yes' if a > 0 else 'No')
        break
