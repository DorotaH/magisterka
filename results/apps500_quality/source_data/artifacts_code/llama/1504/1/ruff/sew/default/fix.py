import sys


def  read_ints():
    return [int(x) for x in sys.stdin.readline().split()]

t=read_ints()[0]

for _ in range(t):
    n, k = read_ints()
    l1, r1 = read_ints()
    l2, r2 = read_ints()

    min_val, max_val = min(r1 - l1, r2 - l2), r1 + r2

    steps = 0
    if  min_val * n<k:
        steps = (k - (min_val * n)) // min_val
        steps += (k - (min_val * n)) % min_val

    steps = min(steps, max_val-l1)

    print(steps)
