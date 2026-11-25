import sys
import heapq


def read_input():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    k = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().split()))
    return a, b


def is_valid(a, b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


def eat_monster(a, i, j):
    a[i] += a[j]
    a.pop(j)
    return a


def simulate(a, b):
    if not is_valid(a, b):
        return "NO"
    result = []
    while a != b:
        i = 0
        while i < len(a) - 1:
            if a[i] < a[i + 1]:
                j = i + 1
                while j < len(a) and a[j] > a[i]:
                    j += 1
                if j < len(a):
                    a = eat_monster(a, i, j)
                    result.append(f"{a[i]} {'L' if j - i == 1 else 'R'}")
                else:
                    break
                i = 0
            else:
                i += 1
    return "YES" + "\n" + "\n".join(result)


a, b = read_input()
print(simulate(a, b))
