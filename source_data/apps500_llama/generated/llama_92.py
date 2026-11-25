import sys

def solve():
    n = int(sys.stdin.readline())

    if n % 2 == 0:
        print(0)
    else:
        print(1)

if __name__ == "__main__":
    solve()
