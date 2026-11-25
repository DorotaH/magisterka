from sys import stdin
from collections import deque

def main():
    n, bulbs = int(stdin.readline()), list(map(lambda x: int(x) if x != '0' else 0, stdin.readline().split()))

    if  0 == n:
        print(0)
        return

    even, odd = deque(), deque()
    for  bulb in  bulbs:
        if  bulb:
            if not bulb % 2 == 0:
                odd.append(bulb)
            else:
                even.append(bulb)

    min_complexity=float('inf')
    while even and odd:
        min_complexity = min(min_complexity, len(even) + len(odd))
        if even[0] < odd[0]:
            min_complexity += 1
            even.popleft()
            odd.popleft()
        else:
            min_complexity += 1
            odd.popleft()
            even.popleft()

    print(min_complexity)

if __name__ == '__main__':
    main()
