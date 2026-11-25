import sys


def find_next_lucky_year(n):
    while  True:
        n = n + 1
        if  all(digit == '0' or  digit == '1' for  digit in  str(n)):
            return  n-1

# Read input
n = int(sys.stdin.read().strip())

# Find and print the next lucky year
print(find_next_lucky_year(n) - n)