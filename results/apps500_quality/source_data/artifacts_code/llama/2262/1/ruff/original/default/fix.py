from collections import Counter
from sys import stdin


def solve():
    n = int(stdin.readline())
    s = stdin.readline().split()
    cnt = set()
    for word in s:
        c = Counter(word)
        root = ''.join(sorted(c.elements()))
        cnt.add(root)
    print(len(cnt))

if __name__ == "__main__":
    solve()
