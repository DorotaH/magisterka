import sys


def main():
    input_values = list(map(int, sys.stdin.readline().split()))
    N, M = input_values[0], input_values[1]
    assignments = list(map(int, sys.stdin.readline().split()))

    # Sort the assignments in ascending order
    assignments.sort()

    # Initialize variables
    total_days = 0
    current_day = 0
    hangout_days = 0

    # Iterate over the assignments
    for days in assignments:
        # If there are enough days left, do the assignment
        if current_day + days <= N:
            current_day += days
            hangout_days += N - current_day
        # If there are not enough days left, we cannot finish all the assignments
        else:
            print(-1)
            return

    print(hangout_days)

if __name__ == "__main__":
    main()
