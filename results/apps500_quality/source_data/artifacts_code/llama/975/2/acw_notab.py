from collections import Counter


def min_flicks(n, sherlock, moriarty):
    counter = Counter(sherlock + moriarty)
    return sum(
        abs(value - (n - counter[digit])) for digit, value in counter.items()
    )


def max_flicks(n, sherlock, moriarty):
    counter = Counter(sherlock + moriarty)
    max_flicks = 0
    for digit in sorted(counter.keys()):
        max_flicks += (n - counter[digit]) * (n - counter[digit]) // 2
        max_flicks -= (counter[digit] - (n - counter[digit])) * (counter[digit] - (n - counter[digit])) // 2
    return max_flicks


n = int(input())
sherlock = input()
moriarty = input()
print(min_flicks(n, sherlock, moriarty))
print(max_flicks(n, sherlock, moriarty))
