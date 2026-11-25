from collections import Counter


def min_flicks(n, sherlock, moriarty):
    digits = sorted(Counter(sherlock + moriarty).items())
    return sum(count // 2 for digit, count in digits)


def max_flicks(n, sherlock, moriarty):
    digits = sorted(Counter(sherlock + moriarty).items())
    return sum(digits[i][1] - digits[i - 1][1] for i in range(1, len(digits)))


n = int(input())
sherlock = input()
moriarty = input()

print(min_flicks(n, sherlock, moriarty))
print(max_flicks(n, sherlock, moriarty))
