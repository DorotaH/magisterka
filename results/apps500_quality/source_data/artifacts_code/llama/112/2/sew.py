from collections import defaultdict
from sys import stdin


def  read_ints():
    return map(int, stdin.readline().split())


def  main():
    n, digits = next(read_ints()), defaultdict(int)
    for _ in range(0, n):
        for face in read_ints():
            digits[face] += 1

    max_num=0
    for i in range(1, 10):
        num=''
        for digit in str(i):
            if  0 == digits[digit]:
                break
            num += digit
            digits[digit] -= 1
        else:
            max_num=max(max_num, int(num))

    print(max_num if  max_num>0 else 0)

if  __name__ == "__main__":
    main()
