import sys

# Read input from standard input
input_str = sys.stdin.readline().strip()
a, b = map(int, input_str.split())

# Check if the input date is valid
if not (
    (a < 1 or a > 12 or b < 1 or b > 31 or (a == 2 and b > 28))
    and (a != 2 or b > 29)
    and (a != 4 and a != 6 and a != 9 and a != 11 and b > 30)
):
    count = sum(1 for m in range(1, a) if m == b) + (1 if b == a else 0)
    print(count)
else:
    # Count the number of Takahashi dates
    print(0)