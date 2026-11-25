from collections import Counter


def flicks(sherlock, moriarty):
    sherlock_count = Counter(sherlock)
    moriarty_count = Counter(moriarty)
    
    min_flicks = 0
    max_flicks = 0
    
    for digit in '0123456789':
        if digit in sherlock_count and digit in moriarty_count:
            min_flicks += min(sherlock_count[digit], moriarty_count[digit])
            max_flicks += max(sherlock_count[digit], moriarty_count[digit]) - min(sherlock_count[digit], moriarty_count[digit])
    
    return min_flicks, max_flicks

# Read input
n = int(input())
sherlock = input().strip()
moriarty = input().strip()

# Calculate and print the results
min_flicks, max_flicks = flicks(sherlock, moriarty)
print(min_flicks)
print(max_flicks)
