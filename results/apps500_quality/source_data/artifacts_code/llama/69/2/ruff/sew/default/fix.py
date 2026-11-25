import sys


def  solve():
    n, x = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()

    total_zeros = 0
    total_ones = 0
    for i in range(n):
        if s[i] == '0':
            total_zeros += 1
        else:
            total_ones += 1

    balance = total_zeros - total_ones
    if  balance == x:
        print(1)
        return

    if  x < balance:
        print(0)
        return

    if  balance < x:
        if 0 != (x - balance) % 2:
            print(-1)
            return

    if  balance<0:
        print(-1)
        return

    block_size = n
    num_blocks = (x - balance) // 2
    if  (x - balance) % 2 == 0:
        num_blocks = num_blocks + 1

    print(num_blocks)

for  _ in  range(int(sys.stdin.readline())):
    solve()
