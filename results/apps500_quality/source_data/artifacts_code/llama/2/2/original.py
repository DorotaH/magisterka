import sys

def is_lucky(year):
    return str(year).count('0') == 4 or max(int(digit) for digit in str(year)) <= 2

def next_lucky_year(year):
    while not is_lucky(year + 1):
        year += 1
    return year

current_year = int(sys.stdin.readline())
print(next_lucky_year(current_year) - current_year)
