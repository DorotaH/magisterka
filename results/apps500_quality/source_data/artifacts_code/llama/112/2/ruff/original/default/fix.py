from collections import defaultdict
from sys import stdin


def read_ints():
    return map(int, stdin.readline().split())

def main():
    n = next(read_ints())
    digits = defaultdict(int)
    for _ in range(n):
        for face in read_ints():
            digits[face] += 1

    max_num = 0
    for i in range(1, 10):
        num = ''
        for digit in str(i):
            if digits[digit] == 0:
                break
            num += digit
            digits[digit] -= 1
        else:
            max_num = max(max_num, int(num))

    print(max(0, max_num))

if __name__ == "__main__":
    main()
