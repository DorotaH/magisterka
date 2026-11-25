import sys
import math

def main():
    a = list(map(int, input().split()))
    n = int(input())
    b = list(map(int, input().split()))

    min_fret = float('inf')
    max_fret = float('-inf')

    for note in b:
        min_fret = min(min_fret, min((note - ai) // 6 + 1 for ai in a))
        max_fret = max(max_fret, max((note - ai) // 6 + 1 for ai in a))

    print(max_fret - min_fret)

if __name__ == "__main__":
    main()
