import sys


def solve(n):
    digits = []
    for i in range(1, n):
        binary = bin(i)[2:]
        if len(binary) > 1:
            digits.append(binary)

    res = 0
    for i, binary in enumerate(digits[::-1]):
        res += int(binary) * (10 ** (len(digits) - i - 1))
        if len(digits) - i - 1 == n - len(digits):
            return str(res)

    return str(res * 10 ** (n - len(digits)))


def main():
    input_lines = sys.stdin.readlines()
    for line in input_lines[1:]:
        n = int(line)
        print(solve(n))


if __name__ == "__main__":
    main()
