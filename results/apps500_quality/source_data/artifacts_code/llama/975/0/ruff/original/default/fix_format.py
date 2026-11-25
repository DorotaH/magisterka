from collections import Counter


def min_flicks(n, sherlock, moriarty):
    digits = sorted(Counter(sherlock + moriarty).items())
    result = 0
    for digit, count in digits:
        result += count // 2
    return result


def max_flicks(n, sherlock, moriarty):
    digits = sorted(Counter(sherlock + moriarty).items())
    result = 0
    for i in range(1, len(digits)):
        result += digits[i][1] - digits[i - 1][1]
    return result


n = int(input())
sherlock = input()
moriarty = input()

print(min_flicks(n, sherlock, moriarty))
print(max_flicks(n, sherlock, moriarty))
