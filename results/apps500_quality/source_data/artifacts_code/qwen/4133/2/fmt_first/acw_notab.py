import sys


def solve(input_string):
    # Initialize variables
    stack = []
    result = []
    i = 0

    while i < len(input_string):
        if input_string[i] == "?":
            # Start of a new sequence
            sequence = []
            i += 1
            while input_string[i] != ">":
                if input_string[i] == "_":
                    # Skip the next character
                    i += 2
                elif input_string[i] in [
                    "0",
                    "1",
                    "2",
                    "3",
                    "4",
                    "5",
                    "6",
                    "7",
                    "8",
                    "9",
                ]:
                    # Add the number to the sequence
                    sequence.append(input_string[i])
                    i += 1
                else:
                    # Invalid character
                    return "false"
            i += 1
            # Add the sequence to the result
            result.append("".join(sequence))
        elif input_string[i] == ".":
            # End of input
            break
        else:
            # Invalid character
            return "false"

    # Sort the result lexicographically
    result.sort()

    # Print the result
    for r in result:
        print(r)


# Read input from standard input
input_string = sys.stdin.read().strip()

# Solve the problem
solve(input_string)
