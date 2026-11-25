from collections import Counter


def min_flicks(n, sherlock, moriarty):
    counter = Counter(sherlock + moriarty)
    min_flicks = 0
    for digit in counter:
        min_flicks = min_flicks + abs(counter[digit] - (n - counter[digit]))
    return min_flicks


def max_flicks(n, sherlock, moriarty):
    counter = Counter(sherlock + moriarty)
    max_flicks = 0
    for digit in sorted(counter.keys()):
        max_flicks = max_flicks + (n - counter[digit]) * (n - counter[digit]) // 2
        max_flicks = (
            max_flicks
            - (counter[digit] - (n - counter[digit]))
            * (counter[digit] - (n - counter[digit]))
            // 2
        )
    return max_flicks


n = int(input())
sherlock, moriarty = input(), input()
print(min_flicks(n, sherlock, moriarty))
print(max_flicks(n, sherlock, moriarty))
