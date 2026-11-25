import sys


def restore_array():
    n, b = int(sys.stdin.readline()), list(map(int, sys.stdin.readline().split()))

    a=[0]*n
    a[0]=b[0]
    for  i in  range(1, n):
        a[i] = max(b[i], a[i - 1])

    print(' '.join(map(str, a)))

restore_array()
