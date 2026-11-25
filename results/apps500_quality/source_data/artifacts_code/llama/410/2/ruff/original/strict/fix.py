import sys


def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

def solve():
    n, = get_ints()
    a = get_list()
    k, = get_ints()
    b = get_list()

    i = 0
    while i < n:
        if a[i] == b[0]:
            break
        i += 1

    if i == n:
        print("NO")
        return

    if i == n-1:
        print("YES")
        print("1 R")
        return

    print("YES")
    ans = []
    while i < n:
        if a[i] < b[0]:
            print("NO")
            return
        if a[i] > b[0]:
            ans.append(str(i+1) + " L")
            a[i] += a[i-1]
            a.pop(i-1)
            n -= 1
        else:
            ans.append(str(i+1) + " R")
            a[i] += a[i+1]
            a.pop(i+1)
            n -= 1
        i -= 1
    while i > 0:
        if a[i] > b[0]:
            ans.append(str(i+1) + " L")
            a[i] += a[i-1]
            a.pop(i-1)
            n -= 1
        else:
            ans.append(str(i+1) + " R")
            a[i] += a[i+1]
            a.pop(i+1)
            n -= 1
        i -= 1
    print('\n'.join(ans))

solve()
