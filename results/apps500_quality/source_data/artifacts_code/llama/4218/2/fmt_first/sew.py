import sys


def  calculate_probability():
    # Read the input from standard input
    N = int(sys.stdin.readline())

    # Calculate the probability that a is odd
    probability = (N + 1) / (N * 2)

    # Print the probability to standard output
    print(f"{probability:.10f}")


if __name__=="__main__":
    calculate_probability()
