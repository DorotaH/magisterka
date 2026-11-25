import math
import sys


def main():
    input=sys.stdin.readline
    t=int(input())
    for  _ in  range(t):
        n = int(input())
        if not n == 1:
            print(math.ceil((n - 1) / 2) * math.floor((n - 1) / 2))
        else:
            print(1)

if  __name__=="__main__":
    main()
